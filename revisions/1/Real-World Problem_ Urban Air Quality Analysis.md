# Real-World Problem: Urban Air Quality Analysis

## Scenario

You are a data analyst working for the 'GreenCity Initiative', an environmental organization focused on improving urban living conditions. Your current project involves analyzing air quality data collected from various monitoring stations across a major city. The goal is to identify patterns, detect anomalies, and provide insights to help the city council make informed decisions about pollution control and public health.

## Data Description

You have been provided with a dataset containing hourly readings from multiple air quality monitoring stations. Each station records the following parameters:

*   **Station ID:** A unique identifier for the monitoring station (e.g., 'S001', 'S002').
*   **Timestamp:** The date and time of the reading (e.g., '2025-07-15 10:00:00').
*   **PM2.5:** Particulate Matter 2.5 concentration (in µg/m³).
*   **PM10:** Particulate Matter 10 concentration (in µg/m³).
*   **O3:** Ozone concentration (in ppb).
*   **NO2:** Nitrogen Dioxide concentration (in ppb).
*   **Temperature:** Ambient temperature (in Celsius).
*   **Humidity:** Relative humidity (in %).

## Objectives

Your task is to perform the following analyses using Python, applying the concepts learned from the provided document:

1.  **Data Loading and Initial Inspection:**
    *   Load the raw data into appropriate Python data structures (lists and NumPy arrays).
    *   Identify the data types of each column.
    *   Perform basic checks on the data (e.g., number of records, number of stations).

2.  **Data Cleaning and Preprocessing:**
    *   Handle missing values (e.g., replace with a suitable measure like the mean or median for numerical data, or a placeholder for categorical data).
    *   Correct any obvious data entry errors or outliers (e.g., negative concentrations, unusually high values).
    *   Convert units if necessary (e.g., convert temperature from Celsius to Fahrenheit if required for a specific analysis).

3.  **Basic Statistical Analysis:**
    *   Calculate descriptive statistics (mean, median, standard deviation, min, max) for each air pollutant (PM2.5, PM10, O3, NO2) across all stations.
    *   Determine the correlation between different pollutants and environmental factors (Temperature, Humidity).

4.  **Station-wise Analysis:**
    *   Identify the station with the highest average PM2.5 concentration.
    *   Identify the station with the lowest average O3 concentration.
    *   For a specific station (e.g., 'S003'), analyze its daily average PM2.5 levels and identify days with concentrations exceeding a certain threshold (e.g., 50 µg/m³).

5.  **Time-series Analysis (Simplified):**
    *   Extract hourly data for a specific pollutant (e.g., PM2.5) for a chosen station over a 24-hour period.
    *   Identify the peak pollution hour for that station.

6.  **Custom Function Development:**
    *   Create a Python function to calculate the Air Quality Index (AQI) for PM2.5 based on a simplified formula (you will be provided with the formula).
    *   Apply this function to the PM2.5 data and categorize air quality levels (Good, Moderate, Unhealthy).

## Deliverables

*   A Python script (`air_quality_analysis.py`) containing all the code for the analysis.
*   A Jupyter Notebook (`air_quality_solution.ipynb`) explaining each step of the analysis, showing the code, outputs, and interpretations. This notebook should serve as a comprehensive solution guide.
*   A simulated dataset (`air_quality_data.csv`) that you will generate to serve as the input for the problem.

