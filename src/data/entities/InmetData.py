import os
import pandas as pd
from typing import Literal

DataType = Literal['Total preciptation (mm)', 'Average atmospheric pressure (mB)', 'Maximum temperature (°C)', 'Average temperature (°C)', 'Minimum temperature (°C)', 'Relative humidity (%)', 'Average wind speed (m/s)']
DataColumn = ['Date', 'Total preciptation (mm)', 'Average atmospheric pressure (mB)', 'Maximum temperature (°C)', 'Average temperature (°C)', 'Minimum temperature (°C)', 'Relative humidity (%)', 'Average wind speed (m/s)']

MonthType = Literal["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov","Dec"]
MonthColumn = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov","Dec"]

class InmetData:
  def __init__(self):
    # This is the path of current file
    self.this_path = os.path.dirname(__file__)
    
    # This is the path of the input folder
    self.input_folder_path = os.path.join(self.this_path, "../../../data/raw/csv/INMET")
    
    # This is the data of cities
    self.cities_data = self._get_cities_data()
    
    # This is the data of stations
    self.stations_data = self._get_stations_data()
    
  def _get_cities_data(self):
    # Create empty dict 
    cities_data = {}
    
    # Get cities folder path
    cities_folder_path = os.path.join(self.input_folder_path, "cities_data")
    
    # Get all files in cities folder
    cities_files = os.listdir(cities_folder_path)
    
    # Iterate over files
    for city_file in cities_files:
      # Get code of city
      city_code = city_file.split('_')[1]
      
      # Get file path
      city_file_path = os.path.join(cities_folder_path, city_file)
      
      # Open file
      city_file_data = pd.read_csv(city_file_path, sep=';')
      
      # Transform NaN, null and empty values to 0
      city_file_data = city_file_data.fillna(int(0))
      
      # Remove last column
      city_file_data = city_file_data.iloc[:, :-1]
      
      # Append data column to dataframe
      city_file_data.columns = DataColumn
      
      # Convert date column to datetime
      city_file_data['Date'] = pd.to_datetime(city_file_data['Date'], format="%Y-%m-%d")
      
      # Set the date column as the index
      city_file_data.set_index('Date', inplace=True)
      
      # Convert other columns to numeric and replace "," to "."
      numeric_columns = city_file_data.columns[0:]
      city_file_data[numeric_columns] = city_file_data[numeric_columns].replace(',','.', regex=True)
      
      # Iterate over numeric column and convert to numeric
      for col in numeric_columns:
        city_file_data[col] = pd.to_numeric(city_file_data[col], errors='coerce')
      
      # Resample the data to monthly frequency and calculate the mean
      monthly_avg_df = city_file_data.resample('ME').mean()
      
      # Renaming the Date column index with month name
      monthly_avg_df.index = monthly_avg_df.index.strftime('%b')
       
      # Append the monthly data to the dict
      cities_data[city_code] = monthly_avg_df
    
    return cities_data
  
  def _get_stations_data(self):
    # Create empty dict
    stations_data = {}
    
    # Get file path
    stations_file_path = os.path.join(self.input_folder_path, "/stations_catalog/stations_catalog.csv")
    
    # Open file
    print(stations_file_path)
    
    