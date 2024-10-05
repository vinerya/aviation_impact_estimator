# Aviation Impact Estimator

This project is the starting point to estimate the impact of airspace closures on the aviation industry, taking into account rerouting considerations. It uses simulated data to model various aspects of air travel and calculates the additional costs and revenue losses associated with closed airspaces.

## Features

1. Data Generation: Creates simulated data for air routes, including origin, destination, flight frequency, passenger numbers, and fuel costs.
2. Rerouting Impact Estimation: Calculates the impact of airspace closures considering:
   - Additional fuel costs due to longer routes
   - Potential revenue loss from cancelled bookings
   - Percentage of routes affected

## Setup

1. Ensure you have Python 3.7+ installed.
2. Clone this repository:
   ```
   git clone https://github.com/vineryae/aviation_impact_estimator.git
   cd aviation_impact_estimator
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the main script:

```
python main.py
```

This will generate simulated data, estimate the impact of airspace closures, and print a summary of the results.

## Project Structure

- `main.py`: Entry point of the application
- `data_loader.py`: Handles data generation and preprocessing
- `models.py`: Contains the impact estimation model
- `README.md`: This file, containing project information and instructions

## Methodology

1. Data Generation: The project creates simulated data for air routes, including:
   - Origin and destination countries
   - Number of daily flights
   - Passengers per flight
   - Revenue per passenger
   - Original and rerouted distances
   - Fuel costs

2. Impact Estimation: Calculates the impact of airspace closures based on:
   - Additional fuel costs for rerouted flights
   - Estimated revenue loss from cancelled bookings (assumed to be 5% of affected routes)
   - Percentage of routes affected by the closures

## Interpreting Results

The impact estimation provides:
- Total daily revenue across all routes
- Total impact (additional costs + revenue loss) due to airspace closures
- Breakdown of additional fuel costs and revenue losses
- Percentage of routes affected by the closures

## Note

This project uses simulated data for demonstration purposes. For real-world application, replace the data generation function in `data_loader.py` with actual data from airlines or aviation authorities. The accuracy of the estimations depends heavily on the quality and comprehensiveness of the input data.

## Future Improvements

For more accurate and useful estimations, consider:
- Incorporating real data from airlines and aviation authorities
- Adding more factors such as crew scheduling impacts, airport capacity changes, and seasonal variations
- Implementing a more sophisticated model for passenger booking cancellations
- Developing a user interface for easier interaction and scenario testing

## Contributing

Contributions to improve the project are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.