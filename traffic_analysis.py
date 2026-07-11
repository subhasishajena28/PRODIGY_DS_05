"""
==========================================================
Traffic Accident Analysis using US Accidents Dataset
Author : Subhasisha Jena
Description:
This project analyzes traffic accident data to identify
patterns related to weather, road conditions, and time.
It also visualizes accident hotspots and contributing factors.
==========================================================
"""

# ===============================
# Import Libraries
# ===============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
import os
import warnings

warnings.filterwarnings("ignore")

# Set plot style
sns.set(style="whitegrid")

# ===============================
# Create Output Folders
# ===============================

os.makedirs("images", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# ===============================
# Load Dataset
# ===============================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv("data/US_Accidents_March23.csv")

print("Dataset Loaded Successfully!")
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

# ===============================
# Data Overview
# ===============================

print("\nFirst Five Records")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum().sort_values(ascending=False).head(15))

# ===============================
# Data Cleaning
# ===============================

print("\nCleaning Dataset...")

required_columns = [
    "Severity",
    "Start_Time",
    "Weather_Condition",
    "Visibility(mi)",
    "Temperature(F)",
    "Humidity(%)",
    "Wind_Speed(mph)",
    "Start_Lat",
    "Start_Lng"
]

df = df.dropna(subset=required_columns)

print("Missing values removed.")
print("Remaining Rows:", len(df))

# ===============================
# Feature Engineering
# ===============================

print("\nCreating Time Features...")

df["Start_Time"] = pd.to_datetime(df["Start_Time"])

df["Hour"] = df["Start_Time"].dt.hour
df["Month"] = df["Start_Time"].dt.month
df["Day"] = df["Start_Time"].dt.day_name()

def time_period(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"

df["Time_of_Day"] = df["Hour"].apply(time_period)

print("Features Created Successfully!")

# ===============================
# Severity Distribution
# ===============================

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="Severity",
    palette="viridis"
)

plt.title("Accident Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Number of Accidents")

plt.tight_layout()

plt.savefig("images/severity_distribution.png")
plt.close()

# ===============================
# Accidents by Hour
# ===============================

plt.figure(figsize=(12,5))

sns.countplot(
    data=df,
    x="Hour",
    color="steelblue"
)

plt.title("Accidents by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("images/accident_by_hour.png")
plt.close()

# ===============================
# Accidents by Day
# ===============================

order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

plt.figure(figsize=(10,5))

sns.countplot(
    data=df,
    x="Day",
    order=order,
    palette="Set2"
)

plt.xticks(rotation=30)

plt.title("Accidents by Day")

plt.tight_layout()

plt.savefig("images/accident_by_day.png")
plt.close()

# ===============================
# Weather Conditions
# ===============================

top_weather = (
    df["Weather_Condition"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(12,6))

sns.barplot(
    x=top_weather.values,
    y=top_weather.index,
    palette="coolwarm"
)

plt.title("Top 10 Weather Conditions")

plt.xlabel("Accident Count")

plt.tight_layout()

plt.savefig("images/accident_by_weather.png")
plt.close()

# ===============================
# Correlation Heatmap
# ===============================

numeric = df[
    [
        "Severity",
        "Temperature(F)",
        "Humidity(%)",
        "Visibility(mi)",
        "Wind_Speed(mph)"
    ]
]

plt.figure(figsize=(8,6))

sns.heatmap(
    numeric.corr(),
    annot=True,
    cmap="YlGnBu"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("images/correlation_heatmap.png")
plt.close()

# ===============================
# Hotspot Map
# ===============================

print("\nGenerating Hotspot Map...")

sample = df.sample(min(8000, len(df)), random_state=42)

m = folium.Map(
    location=[
        sample["Start_Lat"].mean(),
        sample["Start_Lng"].mean()
    ],
    zoom_start=5
)

heat_data = [
    [row["Start_Lat"], row["Start_Lng"]]
    for _, row in sample.iterrows()
]

HeatMap(heat_data).add_to(m)

m.save("outputs/hotspot_map.html")

# ===============================
# Save Summary
# ===============================

summary = pd.DataFrame({
    "Metric": [
        "Total Records",
        "Average Severity",
        "Unique Weather Conditions",
        "Average Temperature",
        "Average Visibility"
    ],
    "Value": [
        len(df),
        round(df["Severity"].mean(),2),
        df["Weather_Condition"].nunique(),
        round(df["Temperature(F)"].mean(),2),
        round(df["Visibility(mi)"].mean(),2)
    ]
})

summary.to_csv(
    "outputs/summary.csv",
    index=False
)

# ===============================
# Key Insights
# ===============================

print("\n")
print("=" * 60)
print("PROJECT SUMMARY")
print("=" * 60)

print(f"Total Accidents       : {len(df)}")
print(f"Average Severity      : {df['Severity'].mean():.2f}")
print(f"Weather Types         : {df['Weather_Condition'].nunique()}")
print(f"Average Temperature   : {df['Temperature(F)'].mean():.2f}")
print(f"Average Visibility    : {df['Visibility(mi)'].mean():.2f}")

print("\nAll visualizations saved inside 'images/' folder.")
print("Hotspot map saved inside 'outputs/' folder.")
print("Summary saved successfully.")

print("=" * 60)
print("Project Completed Successfully!")
print("=" * 60)
