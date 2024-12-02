
# 🚗 **Carbon Footprint Tracker**

A Python-based tool to calculate, save, and visualize the carbon emissions from trips, helping users track their environmental impact. The program includes features like cumulative emissions calculation, trip history storage, and graphical visualization.

---

## 🌟 **Features**
- Calculate carbon emissions for trips based on parameters like distance, fuel type, traffic conditions, and idle time.
- Save trip data to a JSON file for future reference.
- View past trips and cumulative emissions history.
- Plot a graph of cumulative emissions over recorded trips.
- Easy-to-use menu system with options to calculate, view history, and exit.

---

## 📋 **How It Works**
1. **Carbon Emissions Calculation**:
   - Takes inputs like trip distance, number of riders, fuel type, traffic conditions, idle time, and whether it's nighttime.
   - Calculates emissions using predefined constants and adjustments for fuel, traffic, and time of day.

2. **Trip History**:
   - Saves each trip's data to a `JSON` file.
   - Displays a list of all recorded trips with an option to visualize cumulative emissions via a graph.

3. **Visualization**:
   - Uses `matplotlib` to plot a graph of cumulative emissions over multiple trips.

---

## 🛠️ **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/carbon-footprint-tracker.git
   cd carbon-footprint-tracker
   ```

2. Install the required dependencies:
   ```bash
   pip install matplotlib
   ```

3. Run the program:
   ```bash
   python tracker.py
   ```

---

## 🎮 **Usage**

1. **Main Menu**:
   - Choose from the following options:
     1. **Calculate Carbon Emissions**: Enter trip details to calculate and optionally save emissions.
     2. **View Trip History**: See a list of recorded trips and visualize emissions data with a graph.
     3. **Exit**: Quit the program.

2. **Sample Inputs**:
   - Distance (in km): `15`
   - Number of Riders: `2`
   - Fuel Type: `petrol`, `diesel`, or `ev`
   - Traffic Condition: `light`, `moderate`, or `heavy`
   - Idle Time (in minutes): `5`
   - Nighttime (8 PM–6 AM): `yes` or `no`

3. **Outputs**:
   - Emissions for the trip in grams of CO2.
   - Cumulative emissions saved.
   - Option to view a graph of cumulative emissions.

---

## 🖼️ **Screenshots**

### Main Menu:
```
--- Carbon Footprint Tracker Menu ---
1. Calculate Carbon Emissions for a Trip
2. View Trip History
3. Exit
Enter your choice (1/2/3):
```

### Cumulative Emissions Graph:
![Graph Example](example-graph.png)

---

## 📂 **File Structure**
```
carbon-footprint-tracker/
├── tracker.py              # Main Python script
├── carbon_footprint_data.json # JSON file storing trip data
└── README.md               # Project documentation
```

---

## 📈 **Future Enhancements**
- Add a web-based or mobile interface.
- Integrate APIs for real-time traffic and fuel efficiency data.
- Provide CO2 offsets or suggestions to reduce emissions.
- Add export options for trip history (e.g., CSV or PDF).

---

## 🛡️ **License**
This project is licensed under the [MIT License](LICENSE).

---

## 🤝 **Contributing**
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

---

## 🌐 **Connect**
- GitHub: [RAIF-KARANI](https://github.com/RAIF-KARANI)
- Email: karaniraif@gamil.com
