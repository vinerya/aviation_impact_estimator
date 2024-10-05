import data_loader
import models

def main():
    # Load and preprocess data
    data = data_loader.load_data()
    preprocessed_data = data_loader.preprocess_data(data)
    
    # Define closed airspaces (example)
    closed_airspaces = ['USA', 'China']
    
    # Run estimation model
    impact_estimate = models.estimate_impact(preprocessed_data, closed_airspaces)
    
    # Print results
    print("\nImpact Estimation Results:")
    print(f"Total Daily Revenue: ${impact_estimate['total_daily_revenue']:,}")
    print(f"Total Impact: ${impact_estimate['total_impact']:,}")
    print(f"Additional Fuel Cost: ${impact_estimate['additional_fuel_cost']:,}")
    print(f"Revenue Loss: ${impact_estimate['revenue_loss']:,}")
    print(f"Percent of Routes Affected: {impact_estimate['percent_routes_affected']}%")

if __name__ == "__main__":
    main()