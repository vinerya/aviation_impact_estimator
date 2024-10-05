import pandas as pd
from typing import Dict, Any

def estimate_impact(data: pd.DataFrame, closed_airspaces: list) -> Dict[str, Any]:
    """
    Estimates the impact of airspace closure using rerouting data.
    This method considers additional fuel costs and potential revenue loss due to longer routes.
    """
    # Filter routes affected by closed airspaces
    affected_routes = data[(data['origin'].isin(closed_airspaces)) | (data['destination'].isin(closed_airspaces))]
    
    # Calculate additional costs due to rerouting
    total_additional_fuel_cost = affected_routes['additional_fuel_cost'].sum()
    
    # Estimate revenue loss due to longer routes (assuming 2% of passengers cancel)
    revenue_loss = affected_routes['total_daily_revenue'].sum() * 0.02
    
    # Calculate total impact
    total_impact = total_additional_fuel_cost + revenue_loss
    
    # Calculate percentage of routes affected
    percent_routes_affected = len(affected_routes) / len(data) * 100
    
    return {
        'total_daily_revenue': round(data['total_daily_revenue'].sum()),
        'total_impact': round(total_impact),
        'additional_fuel_cost': round(total_additional_fuel_cost),
        'revenue_loss': round(revenue_loss),
        'percent_routes_affected': round(percent_routes_affected, 2)
    }