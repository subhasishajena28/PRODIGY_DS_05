# PRODIGY_DS_05

📌 Project Overview 

Traffic accidents are influenced by several factors such as weather conditions, road visibility, temperature, and time of day.

This project performs **Exploratory Data Analysis (EDA)** on the **US Accidents Dataset** to identify accident patterns and visualize important insights through charts and an interactive hotspot map.

The analysis helps answer questions like:

- What time of day experiences the most accidents?
- Which weather conditions contribute the most?
- How is accident severity distributed?
- Where are accident hotspots located?
- What environmental factors influence accidents?

---

🎯 Objectives

- Clean and preprocess accident data
- Analyze accident trends by time
- Explore weather-related accident patterns
- Study accident severity
- Generate interactive accident hotspot maps
- Visualize important insights using graphs

---

📂 Dataset

**Dataset:** US Accidents (2016–2023)

Contains millions of accident records collected from across the United States.

Features include:

- Severity
- Start Time
- Weather Condition
- Temperature
- Humidity
- Wind Speed
- Visibility
- Latitude
- Longitude
- Road Information

---

📁 Project Structure

```
Traffic-Accident-Analysis/
│
├── data/
│   └── US_Accidents_March23.csv
│
├── images/
│   ├── severity_distribution.png
│   ├── accident_by_hour.png
│   ├── accident_by_day.png
│   ├── accident_by_weather.png
│   └── correlation_heatmap.png
│
├── notebooks/
│   └── Traffic_Accident_Analysis.ipynb
│
├── outputs/
│   ├── hotspot_map.html
│   └── summary.csv
│
├── src/
│   └── traffic_analysis.py
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

⚙️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Cleaning |
| NumPy | Numerical Operations |
| Matplotlib | Visualization |
| Seaborn | Statistical Charts |
| Folium | Interactive Maps |

---

📊 Analysis Performed

✅ Data Cleaning

✅ Missing Value Analysis

✅ Feature Engineering

✅ Time-based Analysis

✅ Weather Analysis

✅ Severity Distribution

✅ Correlation Analysis

✅ Interactive Accident Hotspot Map

---

📈 Visualizations

The project generates the following visualizations automatically:

- Accident Severity Distribution
- Accidents by Hour
- Accidents by Weekday
- Weather Condition Analysis
- Correlation Heatmap
- Interactive Hotspot Map

---

🚀 How to Run

### Clone Repository

```bash
git clone https://github.com/your-username/Traffic-Accident-Analysis.git
```

---

### Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### Run the Project

```bash
python src/traffic_analysis.py
```

---

📊 Expected Outputs

After running the project:

```
images/

✔ severity_distribution.png

✔ accident_by_hour.png

✔ accident_by_day.png

✔ accident_by_weather.png

✔ correlation_heatmap.png

outputs/

✔ hotspot_map.html

✔ summary.csv
```

---

🔍 Key Insights

- Peak accident frequency occurs during commuting hours.
- Rain, fog, and cloudy weather are common during accidents.
- Low visibility contributes to severe accidents.
- Urban regions have higher accident density.
- Weekdays experience more accidents than weekends.

---

💡 Future Improvements

- Machine Learning Accident Severity Prediction
- Interactive Dashboard using Streamlit
- Real-Time Accident Monitoring
- Geographical Clustering
- Predictive Analytics

---

📚 Skills Demonstrated

- Exploratory Data Analysis (EDA)
- Data Cleaning
- Feature Engineering
- Data Visualization
- Geospatial Analysis
- Python Programming
- Statistical Analysis



---

# ⭐ If you found this project useful, don't forget to star the repository!
