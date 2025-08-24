
import pandas as pd
import numpy as np

# 1. Data Loading and Initial Inspection
print("\n--- Data Loading and Initial Inspection ---")
df = pd.read_csv("air_quality_data.csv")
print("DataFrame head:\n", df.head())
print("\nDataFrame info:\n")
df.info()
print("\nNumber of records:", len(df))
print("Number of unique stations:", df["Station ID"].nunique())

# 2. Data Cleaning and Preprocessing
print("\n--- Data Cleaning and Preprocessing ---")
print("Missing values before cleaning:\n", df.isnull().sum())

# Handle missing values: fill numerical NaNs with median, categorical with 'Unknown'
for col in ["PM2.5", "PM10", "O3", "NO2", "Temperature", "Humidity"]:
    df[col].fillna(df[col].median(), inplace=True)

# Correct outliers (e.g., negative concentrations) - already handled during generation, but good to re-check
for col in ["PM2.5", "PM10", "O3", "NO2", "Temperature", "Humidity"]:
    df[col] = df[col].apply(lambda x: max(0, x)) # Ensure non-negative

print("Missing values after cleaning:\n", df.isnull().sum())

# Convert Timestamp to datetime objects
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# 3. Basic Statistical Analysis
print("\n--- Basic Statistical Analysis ---")
pollutants = ["PM2.5", "PM10", "O3", "NO2"]
for pollutant in pollutants:
    print(f"\nDescriptive statistics for {pollutant}:\n{df[pollutant].describe()}")

# Correlation matrix
print("\nCorrelation Matrix (Pollutants and Environmental Factors):\n")
correlation_cols = pollutants + ["Temperature", "Humidity"]
print(df[correlation_cols].corr())

# 4. Station-wise Analysis
print("\n--- Station-wise Analysis ---")
# Station with highest average PM2.5
avg_pm25_by_station = df.groupby("Station ID")["PM2.5"].mean()
highest_pm25_station = avg_pm25_by_station.idxmax()
highest_pm25_value = avg_pm25_by_station.max()
print(f"Station with highest average PM2.5: {highest_pm25_station} ({highest_pm25_value:.2f} µg/m³)")

# Station with lowest average O3
avg_o3_by_station = df.groupby("Station ID")["O3"].mean()
lowest_o3_station = avg_o3_by_station.idxmin()
lowest_o3_value = avg_o3_by_station.min()
print(f"Station with lowest average O3: {lowest_o3_station} ({lowest_o3_value:.2f} ppb)")

# Daily average PM2.5 for a specific station (e.g., S003)
specific_station_id = "S003"
s003_df = df[df["Station ID"] == specific_station_id].copy()
s003_df["Date"] = s003_df["Timestamp"].dt.date
daily_avg_pm25_s003 = s003_df.groupby("Date")["PM2.5"].mean()

threshold = 50
days_exceeding_threshold = daily_avg_pm25_s003[daily_avg_pm25_s003 > threshold]
print(f"\nDays with PM2.5 exceeding {threshold} µg/m³ for Station {specific_station_id}:\n{days_exceeding_threshold}")

# 5. Time-series Analysis (Simplified)
print("\n--- Time-series Analysis (Simplified) ---")
# Hourly PM2.5 for a chosen station (S001) over a 24-hour period (first day)
station_s001_first_day = df[(df["Station ID"] == "S001") & (df["Timestamp"].dt.date == df["Timestamp"].dt.date.min())]
hourly_pm25_s001 = station_s001_first_day.set_index("Timestamp")["PM2.5"].resample("H").mean()

peak_hour_pm25 = hourly_pm25_s001.idxmax().hour
peak_pm25_value = hourly_pm25_s001.max()
print(f"Peak PM2.5 hour for Station S001 on {hourly_pm25_s001.index.min().date()}: {peak_hour_pm25}:00 ({peak_pm25_value:.2f} µg/m³)")

# 6. Custom Function Development: AQI Calculation
print("\n--- Custom Function Development: AQI Calculation ---")
def calculate_aqi_pm25(pm25_concentration):
    # Simplified AQI calculation for PM2.5 (example ranges)
    # This is a highly simplified version for demonstration purposes.
    # Real AQI calculation is more complex and involves breakpoints.
    if pm25_concentration <= 12.0:
        return "Good"
    elif pm25_concentration <= 35.4:
        return "Moderate"
    elif pm25_concentration <= 55.4:
        return "Unhealthy for Sensitive Groups"
    elif pm25_concentration <= 150.4:
        return "Unhealthy"
    elif pm25_concentration <= 250.4:
        return "Very Unhealthy"
    else:
        return "Hazardous"

# Apply the function to PM2.5 data
df["PM2.5_AQI_Category"] = df["PM2.5"].apply(calculate_aqi_pm25)

print("\nPM2.5 AQI Categories distribution:\n", df["PM2.5_AQI_Category"].value_counts())


