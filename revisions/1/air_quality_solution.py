{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Urban Air Quality Analysis: A Comprehensive Solution\n",
    "\n",
    "## Scenario Overview\n",
    "\n",
    "This notebook presents a comprehensive analysis of urban air quality data, addressing a real-world problem for the \'GreenCity Initiative\'. The primary goal is to analyze air quality data from various monitoring stations, identify patterns, detect anomalies, and provide actionable insights for pollution control and public health decisions.\n",
    "\n",
    "## Data Description\n",
    "\n",
    "The dataset contains hourly readings from multiple air quality monitoring stations, including:\n",
    "\n",
    "*   **Station ID:** A unique identifier for the monitoring station (e.g., \'S001\', \'S002\').\n",
    "*   **Timestamp:** The date and time of the reading (e.g., \'2025-07-15 10:00:00\').\n",
    "*   **PM2.5:** Particulate Matter 2.5 concentration (in µg/m³).\n",
    "*   **PM10:** Particulate Matter 10 concentration (in µg/m³).\n",
    "*   **O3:** Ozone concentration (in ppb).\n",
    "*   **NO2:** Nitrogen Dioxide concentration (in ppb).\n",
    "*   **Temperature:** Ambient temperature (in Celsius).\n",
    "*   **Humidity:** Relative humidity (in %).\n",
    "\n",
    "## Objectives\n",
    "\n",
    "The analysis covers the following key objectives:\n",
    "\n",
    "1.  **Data Loading and Initial Inspection:** Loading data, identifying types, and basic checks.\n",
    "2.  **Data Cleaning and Preprocessing:** Handling missing values and outliers.\n",
    "3.  **Basic Statistical Analysis:** Calculating descriptive statistics and correlations.\n",
    "4.  **Station-wise Analysis:** Identifying station-specific trends and anomalies.\n",
    "5.  **Time-series Analysis (Simplified):** Analyzing hourly and daily patterns.\n",
    "6.  **Custom Function Development:** Creating and applying a function for Air Quality Index (AQI) calculation.\n",
    "\n",
    "---\n",
    "\n",
    "## 1. Data Loading and Initial Inspection\n",
    "\n",
    "First, we load the `air_quality_data.csv` file into a Pandas DataFrame and perform an initial inspection to understand its structure and content. This step is crucial for familiarizing ourselves with the dataset and identifying any immediate issues.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# Load the dataset\n",
    "df = pd.read_csv(\"air_quality_data.csv\")\n",
    "\n",
    "# Display the first few rows of the DataFrame\n",
    "print(\"DataFrame head:\\\n\", df.head())\n",
    "\n",
    "# Display concise summary of the DataFrame, including data types and non-null values\n",
    "print(\"\\\nDataFrame info:\\\n\")\n",
    "df.info()\n",
    "\n",
    "# Check the number of records and unique stations\n",
    "print(\"\\\nNumber of records:\", len(df))\n",
    "print(\"Number of unique stations:\", df[\"Station ID\"].nunique())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "---\n",
    "\n",
    "## 2. Data Cleaning and Preprocessing\n",
    "\n",
    "Data cleaning is a critical step to ensure the accuracy and reliability of our analysis. In this section, we address missing values and potential outliers. Missing numerical values will be imputed using the median, and a basic check for non-negative concentrations will be performed.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"Missing values before cleaning:\\\n\", df.isnull().sum())\n",
    "\n",
    "# Handle missing values: fill numerical NaNs with median\n",
    "for col in [\"PM2.5\", \"PM10\", \"O3\", \"NO2\", \"Temperature\", \"Humidity\"]:\n",
    "    df[col].fillna(df[col].median(), inplace=True)\n",
    "\n",
    "# Ensure values are non-negative (basic outlier correction)\n",
    "for col in [\"PM2.5\", \"PM10\", \"O3\", \"NO2\", \"Temperature\", \"Humidity\"]:\n",
    "    df[col] = df[col].apply(lambda x: max(0, x))\n",
    "\n",
    "print(\"Missing values after cleaning:\\\n\", df.isnull().sum())\n",
    "\n",
    "# Convert \'Timestamp\' column to datetime objects for easier time-based analysis\n",
    "df[\"Timestamp\"] = pd.to_datetime(df[\"Timestamp\"])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "---\n",
    "\n",
    "## 3. Basic Statistical Analysis\n",
    "\n",
    "Here, we compute descriptive statistics for the air pollutants and analyze the correlation between different pollutants and environmental factors. This provides a foundational understanding of the data distribution and relationships.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pollutants = [\"PM2.5\", \"PM10\", \"O3\", \"NO2\"]\n",
    "for pollutant in pollutants:\n",
    "    print(f\"\\\nDescriptive statistics for {pollutant}:\\\n{df[pollutant].describe()}\")\n",
    "\n",
    "# Calculate and display the correlation matrix\n",
    "print(\"\\\nCorrelation Matrix (Pollutants and Environmental Factors):\\\n\")\n",
    "correlation_cols = pollutants + [\"Temperature\", \"Humidity\"]\n",
    "print(df[correlation_cols].corr())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "---\n",
    "\n",
    "## 4. Station-wise Analysis\n",
    "\n",
    "This section focuses on analyzing data at the individual station level. We will identify stations with the highest and lowest average pollutant concentrations and examine daily trends for a specific station.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Station with highest average PM2.5\n",
    "avg_pm25_by_station = df.groupby(\"Station ID\")[\"PM2.5\"].mean()\n",
    "highest_pm25_station = avg_pm25_by_station.idxmax()\n",
    "highest_pm25_value = avg_pm25_by_station.max()\n",
    "print(f\"Station with highest average PM2.5: {highest_pm25_station} ({highest_pm25_value:.2f} µg/m³)\")\n",
    "\n",
    "# Station with lowest average O3\n",
    "avg_o3_by_station = df.groupby(\"Station ID\")[\"O3\"].mean()\n",
    "lowest_o3_station = avg_o3_by_station.idxmin()\n",
    "lowest_o3_value = avg_o3_by_station.min()\n",
    "print(f\"Station with lowest average O3: {lowest_o3_station} ({lowest_o3_value:.2f} ppb)\")\n",
    "\n",
    "# Daily average PM2.5 for a specific station (e.g., S003)\n",
    "specific_station_id = \"S003\"\n",
    "s003_df = df[df[\"Station ID\"] == specific_station_id].copy()\n",
    "s003_df[\"Date\"] = s003_df[\"Timestamp\"].dt.date\n",
    "daily_avg_pm25_s003 = s003_df.groupby(\"Date\")[\"PM2.5\"].mean()\n",
    "\n",
    "threshold = 50\n",
    "days_exceeding_threshold = daily_avg_pm25_s003[daily_avg_pm25_s003 > threshold]\n",
    "print(f\"\\\nDays with PM2.5 exceeding {threshold} µg/m³ for Station {specific_station_id}:\\\n{days_exceeding_threshold}\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "---\n",
    "\n",
    "## 5. Time-series Analysis (Simplified)\n",
    "\n",
    "This section provides a simplified time-series analysis, focusing on hourly patterns of a specific pollutant for a chosen station. We will identify the peak pollution hour.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Hourly PM2.5 for a chosen station (S001) over a 24-hour period (first day)\n",
    "station_s001_first_day = df[(df[\"Station ID\"] == \"S001\") & (df[\"Timestamp\"].dt.date == df[\"Timestamp\"].dt.date.min())]\n",
    "hourly_pm25_s001 = station_s001_first_day.set_index(\"Timestamp\")[\"PM2.5\"].resample(\"H\").mean()\n",
    "\n",
    "peak_hour_pm25 = hourly_pm25_s001.idxmax().hour\n",
    "peak_pm25_value = hourly_pm25_s001.max()\n",
    "print(f\"Peak PM2.5 hour for Station S001 on {hourly_pm25_s001.index.min().date()}: {peak_hour_pm25}:00 ({peak_pm25_value:.2f} µg/m³)\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "---\n",
    "\n",
    "## 6. Custom Function Development: AQI Calculation\n",
    "\n",
    "Finally, we develop a custom Python function to calculate a simplified Air Quality Index (AQI) for PM2.5 concentrations. This function categorizes air quality into different levels, providing a more intuitive understanding of pollution levels.\n",
    "\n",
    "**Simplified AQI Formula for PM2.5 (for demonstration purposes):**\n",
    "\n",
    "*   0-12.0 µg/m³: Good\n",
    "*   12.1-35.4 µg/m³: Moderate\n",
    "*   35.5-55.4 µg/m³: Unhealthy for Sensitive Groups\n",
    "*   55.5-150.4 µg/m³: Unhealthy\n",
    "*   150.5-250.4 µg/m³: Very Unhealthy\n",
    "*   250.5+ µg/m³: Hazardous\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_aqi_pm25(pm25_concentration):\n",
    "    if pm25_concentration <= 12.0:\n",
    "        return \"Good\"\n",
    "    elif pm25_concentration <= 35.4:\n",
    "        return \"Moderate\"\n",
    "    elif pm25_concentration <= 55.4:\n",
    "        return \"Unhealthy for Sensitive Groups\"\n",
    "    elif pm25_concentration <= 150.4:\n",
    "        return \"Unhealthy\"\n",
    "    elif pm25_concentration <= 250.4:\n",
    "        return \"Very Unhealthy\"\n",
    "    else:\n",
    "        return \"Hazardous\"\n",
    "\n",
    "# Apply the function to the PM2.5 data and display the distribution of AQI categories\n",
    "df[\"PM2.5_AQI_Category\"] = df[\"PM2.5\"].apply(calculate_aqi_pm25)\n",
    "print(\"\\\nPM2.5 AQI Categories distribution:\\\n\", df[\"PM2.5_AQI_Category\"].value_counts())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "---\n",
    "\n",
    "## Conclusion\n",
    "\n",
    "This analysis demonstrates how Python, along with libraries like Pandas and NumPy, can be effectively used to tackle real-world data analysis problems, from data loading and cleaning to statistical analysis and custom function development. The insights gained from such analyses are invaluable for informed decision-making in environmental management and public health.\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0rc1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

