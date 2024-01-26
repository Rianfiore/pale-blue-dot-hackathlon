from typing import Dict, Literal
import pandas as pd
import os
import json

AgriculturalType = Literal['production', 'average_income']
AgriculturalColumns = ['production', 'average_income']

MonthType = Literal['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
MonthColumns = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec']

FederationType = Literal["BR","RO","AC","AM","RR","PA","AP","TO","MA","PI","CE","RN","PB","PE","AL","SE","BA","MG","ES","RJ","SP","PR","SC","RS","MS","MT","GO","DF"];
FederationColumns = ["BR","RO","AC","AM","RR","PA","AP","TO","MA","PI","CE","RN","PB","PE","AL","SE","BA","MG","ES","RJ","SP","PR","SC","RS","MS","MT","GO","DF"];

ProductType = Literal["Cereals, Legumes, and Oilseeds","Cotton","Peanuts (1st Crop)","Peanuts (2nd Crop)","Rice","Oats","Rye","Barley","Beans (1st Crop)","Beans (2nd Crop)","Beans (3rd Crop)","Sunflower","Castor Bean","Corn (1st Crop)","Corn (2nd Crop)","Soybeans","Sorghum","Wheat","Triticale","Pineapple","Garlic","Banana","Potato (1st Crop)","Potato (2nd Crop)","Potato (3rd Crop)","Cocoa","Coffee Total","Arabica Coffee","Robusta Coffee","Sugarcane","Cashew Nut","Onion","Coconut","Tobacco","Guarana","Jute","Orange","Apple","Mallow","Cassava","Black Pepper","Sisal or Agave","Tomato","Grapes"];
ProductColumns = ["Cereals, Legumes, and Oilseeds","Cotton","Peanuts (1st Crop)","Peanuts (2nd Crop)","Rice","Oats","Rye","Barley","Beans (1st Crop)","Beans (2nd Crop)","Beans (3rd Crop)","Sunflower","Castor Bean","Corn (1st Crop)","Corn (2nd Crop)","Soybeans","Sorghum","Wheat","Triticale","Pineapple","Garlic","Banana","Potato (1st Crop)","Potato (2nd Crop)","Potato (3rd Crop)","Cocoa","Coffee Total","Arabica Coffee","Robusta Coffee","Sugarcane","Cashew Nut","Onion","Coconut","Tobacco","Guarana","Jute","Orange","Apple","Mallow","Cassava","Black Pepper","Sisal or Agave","Tomato","Grapes"];

AgriculturalTypeDict = Dict[MonthType, Dict[FederationType, Dict[ProductType, pd.DataFrame]]]
AgriculturalProductionDict = Dict[AgriculturalType, AgriculturalTypeDict]

class AgriculturalProductionData:

  def __init__(self):
    self.input_path = os.path.join(os.path.dirname(__file__), "../../../data/raw/csv/IBGE/agricultural_production/")
    self.output_path = os.path.join(os.path.dirname(__file__), "../../../data/processed/json/IBGE/agricultural_production/")

    self.production_data = pd.read_csv(self.input_path + "production.csv", sep=",", header=None)
    self.average_income_data = pd.read_csv(self.input_path + "average_income.csv", sep=",", header=None)

    production_df = self._format_df(self.production_data)
    average_income_df = self._format_df(self.average_income_data)

    self.agricultural_production_data: AgriculturalProductionDict = {
      "production": production_df,
      "average_income": average_income_df
    }
  def _format_df(self, df: pd.DataFrame) -> AgriculturalTypeDict:

    # Create empty dict to store data
    df_data: AgriculturalTypeDict = {}

    # Removing first 5 rows
    df = df.iloc[5:]

    # Reseting index
    df = df.reset_index(drop=True)

    # Remove last row
    df = df[:-1]

    # Removing NaN, blank spaces and special characters from the dataframe
    df = df.replace(to_replace=r'^(-|NaN|...|\s*)$', value='0', regex=True)

    # data per month
    COLUMNS_PER_MONTH = 44

    # First column index as federation name
    FEDERATION_NAME_INDEX = 0

    # Remove federation column from dataframe
    df = df.drop(df.columns[FEDERATION_NAME_INDEX], axis=1)

    # Iterate over the dataframe
    for i in range(0, len(df.columns), COLUMNS_PER_MONTH):
      # Get the current month
      month = MonthColumns[int(i/COLUMNS_PER_MONTH)]

      # Append month to dict
      df_data[month] = {}

      # Isolate the current month dataframe
      month_df = df.iloc[:, i:i+COLUMNS_PER_MONTH]

      # Append the product columns
      month_df.columns = ProductColumns

      # Iterate over the federation column
      for federation_index in range(0, len(FederationColumns), 1):

        # Get data of current federation
        federation_data = month_df.iloc[federation_index]

        # Append data to dict
        df_data[month][FederationColumns[federation_index]] = federation_data


    return df_data
  
  def save_df(self):
    # Create json object
    agricultural_production_json: AgriculturalProductionDict = {}
    
    # Iterate over the agricultural type
    for agricultural_type in self.agricultural_production_data:
      # Append agricultural type to json object
      agricultural_production_json[agricultural_type] = {}

      # Iterate over the months
      for month in self.agricultural_production_data[agricultural_type]:
        # Append month to json object
        agricultural_production_json[agricultural_type][month] = {}

        # Iterate over the federation
        for federation in self.agricultural_production_data[agricultural_type][month]:
          # Convert the product dataframe to dict
          product_dict = self.agricultural_production_data[agricultural_type][month][federation].to_dict()
          # Append federation to json object
          agricultural_production_json[agricultural_type][month][federation] = product_dict

        

    # Save the json object to a file
    with open(self.output_path + "agricultural_production.json", "w", encoding='utf-8') as outfile:
      json.dump(agricultural_production_json, outfile, indent=2,ensure_ascii=False)
    
  def get_dict(self) -> AgriculturalProductionDict:
    try:
      with open(self.output_path + "agricultural_production.json", "r", encoding='utf-8') as json_file:
        # Load json file
        agricultural_production_json: AgriculturalProductionDict = json.load(json_file)

        # Create dict to store data
        dict_output: AgriculturalProductionDict = {}

        # Iterate over the agricultural type
        for agricultural_type in agricultural_production_json:
          # Append agricultural type to dict
          dict_output[agricultural_type] = {}


          # Iterate over the months
          for month in agricultural_production_json[agricultural_type]:
            
            # Append month to dict
            dict_output[agricultural_type][month] = {}

            # Get the federation dict
            federation_dict = agricultural_production_json[agricultural_type][month]

            # Convert the federation dict to dataframe, using federation dict as columns
            federation_df = pd.DataFrame.from_dict(federation_dict, orient='index')


            # Iterate over the federation columns
            for federation_index in range(0, len(FederationColumns), 1):
              # Get the federation dataframe
              federation_data = federation_df.iloc[federation_index]

              # Append federation dataframe to dict
              dict_output[agricultural_type][month][FederationColumns[federation_index]] = federation_data

        return dict_output
    except Exception as e:
      print(f"Outer exception caught: {e}")
      return None