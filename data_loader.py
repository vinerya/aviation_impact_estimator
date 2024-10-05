import pandas as pd
import numpy as np

def load_data(num_routes=1000):
    np.random.seed(42)
    
    data = {
        'route_id': range(num_routes),
        'origin': np.random.choice(['USA', 'China', 'UK', 'Germany', 'France', 'Japan', 'Canada', 'Australia', 'Brazil', 'India'], num_routes),
        'destination': np.random.choice(['USA', 'China', 'UK', 'Germany', 'France', 'Japan', 'Canada', 'Australia', 'Brazil', 'India'], num_routes),
        'daily_flights': np.random.randint(1, 20, num_routes),
        'passengers_per_flight': np.random.randint(100, 400, num_routes),
        'revenue_per_passenger': np.random.uniform(200, 1000, num_routes),
        'original_distance': np.random.randint(500, 10000, num_routes),
        'fuel_cost_per_km': np.random.uniform(10, 20, num_routes),
    }
    
    # Ensure reroute distance is always greater than or equal to original distance
    data['reroute_distance'] = data['original_distance'] + np.random.randint(0, 2000, num_routes)
    
    return pd.DataFrame(data)

def preprocess_data(df):
    df['total_daily_revenue'] = df['daily_flights'] * df['passengers_per_flight'] * df['revenue_per_passenger']
    df['original_fuel_cost'] = df['original_distance'] * df['fuel_cost_per_km']
    df['reroute_fuel_cost'] = df['reroute_distance'] * df['fuel_cost_per_km']
    df['additional_fuel_cost'] = df['reroute_fuel_cost'] - df['original_fuel_cost']
    return df