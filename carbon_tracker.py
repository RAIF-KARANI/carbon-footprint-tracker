import json
import matplotlib.pyplot as plt

# Constants
CO2_PER_KM = 251  # grams
IDLE_EMISSIONS_PER_MIN = 10  # grams


def calculate_emissions(distance, riders, fuel_type, traffic, idle_time, is_nighttime):
    # Adjustments
    fuel_adjustment = {
        "petrol": 1.0,
        "diesel": 1.15,
        "ev": 0.0
    }.get(fuel_type.lower(), 1.0)

    traffic_adjustment = {
        "light": 1.0,
        "moderate": 1.10,
        "heavy": 1.20
    }.get(traffic.lower(), 1.0)

    idle_emissions = idle_time * IDLE_EMISSIONS_PER_MIN
    nighttime_adjustment = 0.95 if is_nighttime else 1.0

    # CO2 Savings formula
    emissions = (distance * CO2_PER_KM * fuel_adjustment * traffic_adjustment * nighttime_adjustment)
    emissions_per_rider = emissions / riders if riders > 0 else emissions
    total_emissions = emissions_per_rider + idle_emissions

    return round(total_emissions, 2)


def plot_emissions(cumulative_emissions_list):
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, len(cumulative_emissions_list) + 1), cumulative_emissions_list, marker='o', linestyle='-',
             color='b')
    plt.title('Cumulative Emissions Over Trips', fontsize=14)
    plt.xlabel('Trip Number', fontsize=12)
    plt.ylabel('Cumulative Emissions (grams)', fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def view_history():
    try:
        with open("carbon_footprint_data.json", "r") as file:
            cumulative_emissions_list = []
            print("\n--- Trip History ---")
            for idx, line in enumerate(file, start=1):
                trip = json.loads(line)
                print(f"Trip {idx}: {trip}")
                cumulative_emissions_list.append(trip["emissions_saved"])

            # Option to plot graph
            if cumulative_emissions_list:
                plot_graph = input("\nDo you want to see the cumulative emissions graph from the history? (yes/no): ").strip().lower()
                if plot_graph == "yes":
                    plot_emissions(cumulative_emissions_list)
    except FileNotFoundError:
        print("\nNo history available. No trips recorded yet.")


def main():
    cumulative_savings = 0
    cumulative_emissions_list = []
    trip_count = 0

    while True:
        print("\n--- Carbon Footprint Tracker Menu ---")
        print("1. Calculate Carbon Emissions for a Trip")
        print("2. View Trip History")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            # Calculate emissions for a trip
            try:
                distance = float(input("\nEnter trip distance (in km): "))
                riders = int(input("Enter number of riders: "))
                fuel_type = input("Enter fuel type (petrol/diesel/ev): ").strip().lower()
                traffic = input("Enter traffic condition (light/moderate/heavy): ").strip().lower()
                idle_time = int(input("Enter idle time (in minutes): "))
                is_nighttime = input("Is the trip during nighttime (8 PM–6 AM)? (yes/no): ").strip().lower() == "yes"

                emissions_saved = calculate_emissions(distance, riders, fuel_type, traffic, idle_time, is_nighttime)
                print(f"\nEmissions for this trip: {emissions_saved} grams of CO2")

                cumulative_savings += emissions_saved
                cumulative_emissions_list.append(cumulative_savings)
                trip_count += 1
                print(f"Cumulative Emissions Saved: {round(cumulative_savings, 2)} grams of CO2")
                print(f"Total Trips Recorded: {trip_count}")

                # Save results
                save = input("\nDo you want to save this trip's data? (yes/no): ").strip().lower()
                if save == "yes":
                    data = {
                        "distance": distance,
                        "riders": riders,
                        "fuel_type": fuel_type,
                        "traffic": traffic,
                        "idle_time": idle_time,
                        "is_nighttime": is_nighttime,
                        "emissions_saved": cumulative_savings
                    }
                    with open("carbon_footprint_data.json", "a") as file:
                        json.dump(data, file)
                        file.write("\n")
                    print("Trip data saved successfully.")

                # Plot emissions graph
                plot_graph = input("\nDo you want to see the cumulative emissions graph? (yes/no): ").strip().lower()
                if plot_graph == "yes":
                    plot_emissions(cumulative_emissions_list)

            except ValueError:
                print("Invalid input. Please try again.")

        elif choice == "2":
            # View trip history
            view_history()

        elif choice == "3":
            # Exit the program
            print("\nExiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
