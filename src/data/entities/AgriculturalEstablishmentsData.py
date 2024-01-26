from typing import Dict, Literal
import pandas as pd
import os
import json

TypologyType = Literal['Non-Family farming', 'Family farming']
TypologyColumns = ['Non-Family farming', 'Family farming']

FederationType = Literal["Brasil",  "Rondônia",  "Acre",  "Amazonas",  "Roraima",  "Pará",  "Amapá",  "Tocantins",  "Maranhão",  "Piauí",  "Ceará",  "Rio Grande do Norte",  "Paraíba",  "Pernambuco",  "Alagoas",  "Sergipe",  "Bahia",  "Minas Gerais",  "Espírito Santo",  "Rio de Janeiro",  "São Paulo",  "Paraná",  "Santa Catarina",  "Rio Grande do Sul",  "Mato Grosso do Sul",  "Mato Grosso",  "Goiás", "Distrito Federal"]
FederationColumns = ["Brasil",  "Rondônia",  "Acre",  "Amazonas",  "Roraima",  "Pará",  "Amapá",  "Tocantins",  "Maranhão",  "Piauí",  "Ceará",  "Rio Grande do Norte",  "Paraíba",  "Pernambuco",  "Alagoas",  "Sergipe",  "Bahia",  "Minas Gerais",  "Espírito Santo",  "Rio de Janeiro",  "São Paulo",  "Paraná",  "Santa Catarina",  "Rio Grande do Sul",  "Mato Grosso do Sul",  "Mato Grosso",  "Goiás", "Distrito Federal"]

ProductType = Literal['Total', 'Sugarcane spirit', 'Feather cotton', 'Cottonseed', 'Grain rice', 'Roasted coffee beans', 'Ground roast coffee', 'Cajuína', 'Milk cream', 'Candies and jellies', 'Mandioca flour', 'Corn meal', 'Fumo em rolo', 'Vegetables (processed)', 'Liqueurs', 'Butter', 'Molasses', 'Vegetable oils', 'Breads, cakes and cookies', 'Fruit pulp', 'Cheese and cottage cheese', 'Rapadura', 'Fruit juices', 'Grape wine', 'Beef meat (pasture-raised)', 'Pork (pasture-raised)', 'Meat from other animals (pasture-raised)', 'Treated meat (sun-dried meat, salty meat)', 'Sausage and hot dog', 'Leathers and skins', 'Charcoal', 'Wood products', 'Other products', 'Gum or tapioca']
ProductColumns = ['Total', 'Sugarcane spirit', 'Feather cotton', 'Cottonseed', 'Grain rice', 'Roasted coffee beans', 'Ground roast coffee', 'Cajuína', 'Milk cream', 'Candies and jellies', 'Mandioca flour', 'Corn meal', 'Fumo em rolo', 'Vegetables (processed)', 'Liqueurs', 'Butter', 'Molasses', 'Vegetable oils', 'Breads, cakes and cookies', 'Fruit pulp', 'Cheese and cottage cheese', 'Rapadura', 'Fruit juices', 'Grape wine', 'Beef meat (pasture-raised)', 'Pork (pasture-raised)', 'Meat from other animals (pasture-raised)', 'Treated meat (sun-dried meat, salty meat)', 'Sausage and hot dog', 'Leathers and skins', 'Charcoal', 'Wood products', 'Other products', 'Gum or tapioca']

EconomicActivityGroupsType = Literal['Total', 'Production of temporary crops', 'Horticulture and floriculture', 'Production of permanent crops', 'Production of certified seeds and seedlings', 'Livestock and breeding of other animals', 'Forestry production - planted forest', 'Forestry production - native forest', 'Fishing', 'Aquaculture']
EconomicActivityGroupsColumns = ['Total', 'Production of temporary crops', 'Horticulture and floriculture', 'Production of permanent crops', 'Production of certified seeds and seedlings', 'Livestock and breeding of other animals', 'Forestry production - planted forest', 'Forestry production - native forest', 'Fishing', 'Aquaculture']

AgriculturalEstablishmentsDict = Dict[TypologyType, Dict[FederationType, Dict[ProductType, Dict[EconomicActivityGroupsType, pd.DataFrame]]]]
class AgriculturalEstablishmentsData:

  def __init__(self):
    self.input_path = os.path.join(os.path.dirname(__file__), "../../../data/raw/csv/IBGE/agricultural_establishments/")
    self.output_path = os.path.join(os.path.dirname(__file__), "../../../data/processed/json/IBGE/agricultural_establishments/")

    self.establishments_data = pd.read_csv(self.input_path + "agricultural_establishments.csv", sep=",", header=None)
    self.establishments_data = self._format_df(self.establishments_data)


  def _format_df(self, df: pd.DataFrame) -> AgriculturalEstablishmentsDict:
    # Removing first 7 rows
    df = df.iloc[7:,2:]

    # Removing last row
    df = df[:-1]

    # Reseting index
    df = df.reset_index(drop=True)

    # Removing NaN, blank spaces and special characters from the dataframe
    df = df.replace(to_replace=r'NaN|-|\.\.', value='0', regex=True)
    
    # Get step size for each typology
    PRODUCTS_PER_TYPOLOGY = len(ProductColumns)

    # Get columns size of the dataframe
    df_columns_size = len(df.columns)

    # Get rows size of the dataframe
    df_rows_size = len(df.index)

    # Get dict to store all data
    agricultural_establishments_dict = {}

    # Iterate over the dataframe products
    for product_index in range(0, df_columns_size, PRODUCTS_PER_TYPOLOGY):
      # Get data of typology
      products_by_typology = df.iloc[:,product_index:product_index+PRODUCTS_PER_TYPOLOGY]

      # Get typology index
      TYPOLOGY_INDEX =  int(product_index / PRODUCTS_PER_TYPOLOGY) 

      # Get step size for each federation
      ECONOMIC_ACTIVITY_GROUPS_PER_FEDERATION = len(EconomicActivityGroupsColumns)

      # Create dict to store data
      agricultural_establishments_dict[TypologyColumns[TYPOLOGY_INDEX]] = {}

      for economic_activity_index in range(0, df_rows_size, ECONOMIC_ACTIVITY_GROUPS_PER_FEDERATION):
        # Get federation index
        FEDERATION_INDEX = int(economic_activity_index / ECONOMIC_ACTIVITY_GROUPS_PER_FEDERATION)

        # Get federation name
        federation_name = FederationColumns[FEDERATION_INDEX]

        # Get data of federation
        economic_activity_groups_by_federation = products_by_typology.iloc[economic_activity_index:economic_activity_index+ECONOMIC_ACTIVITY_GROUPS_PER_FEDERATION,:]

        # Apply name to the all columns
        economic_activity_groups_by_federation.columns = ProductColumns
        
        # #Apply name to the all rows
        economic_activity_groups_by_federation.index = EconomicActivityGroupsColumns

        # Add data to the dict
        agricultural_establishments_dict[TypologyColumns[TYPOLOGY_INDEX]][federation_name] = economic_activity_groups_by_federation


    return agricultural_establishments_dict
  
  def save_df(self):

    # Create json object
    agricultural_establishments_json = {}

    # Iterate over the dict
    for typology in self.establishments_data:
      # Create dict to store data
      agricultural_establishments_json[typology] = {}

      # Iterate over the dict
      for federation in self.establishments_data[typology]:
        agricultural_establishments_json[typology][federation] = {}

        # Get rows of the current dataframe
        df_rows = self.establishments_data[typology][federation].index

        # Iterate over the dataframe
        for economic_activity_group in df_rows:

          # Get dataframe of the current economic activity group
          df_of_current_economic_activity_group = self.establishments_data[typology][federation].loc[economic_activity_group]

          # Convert the dataframe into json
          json_string = df_of_current_economic_activity_group.to_json( force_ascii=False, indent=2)

          # Create dict to store data
          agricultural_establishments_json[typology][federation][economic_activity_group] = json.loads(json_string)        

    # Save the json object to a file
    with open(self.output_path + "agricultural_establishments.json", "w", encoding='utf-8') as outfile:
      json.dump(agricultural_establishments_json, outfile, indent=2,ensure_ascii=False)
  
  def get_dict(self):
    
    with open(self.output_path + "agricultural_establishments.json", "r", encoding='utf-8') as json_file:
      # Load json file
      json_string: AgriculturalEstablishmentsDict = json.load(json_file)

      # Create dict to store data
      dict_output: AgriculturalEstablishmentsDict = {}

      # Iterate over the dict
      for typology in json_string:

        # Create dict to store data
        dict_output[typology] = {}

        # Iterate over the dict
        for federation in json_string[typology]:
          

          # Create the dataframe
          df = pd.DataFrame.from_dict(json_string[typology][federation], orient='index')

          # Add dataframe to the dict
          dict_output[typology][federation] = df

      return dict_output

      
