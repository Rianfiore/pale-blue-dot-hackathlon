import pandas as pd
import numpy as np
import os

this_path = os.path.dirname(__file__)

class InmetData:
    def __init__(self):
        self.input_path = os.path.join(this_path, "../../../data/raw/csv/Dados_INMET/dados_B803_D_2023-01-01_2023-12-31.csv")
        self.columns = ['Data Medicao', 'PRECIPITACAO TOTAL, DIARIO (AUT)(mm)', 'PRESSAO ATMOSFERICA MEDIA DIARIA (AUT)(mB)', 'TEMPERATURA MAXIMA, DIARIA (AUT)(°C)','TEMPERATURA MEDIA, DIARIA (AUT)(°C)','TEMPERATURA MINIMA, DIARIA (AUT)(°C)','UMIDADE RELATIVA DO AR, MEDIA DIARIA (AUT)(%)','VENTO, VELOCIDADE MEDIA DIARIA (AUT)(m/s)']
        self.dataframe = pd.read_csv(self.input_path, parse_dates=["Data Medicao"],sep=';', usecols=self.columns)

    def show_datafrae(self):
        print(self.dataframe)

    def __fix_null_data(self):
        counter = 1
        while counter < 8:
            for index, value in enumerate(self.dataframe[self.columns[counter]]):
                if isinstance(value, str) and value.strip():
                    self.dataframe[self.columns[counter]].at[index] = float(value.replace(',', '.'))
            counter += 1

        counter = 1
        while counter < 8:
            for index, value in enumerate(self.dataframe[self.columns[counter]]):
                if np.isnan(value):  # Verifica se a string não está vazia 
                    mean = self.dataframe[self.columns[counter]].mean()
                    self.dataframe[self.columns[counter]].at[index] = mean
            counter += 1

    def __get_mean(self, column):
        # Fixing null data
        self.__fix_null_data()

        # Getting monthly means on specific column
        monthly_means = self.dataframe.groupby(self.dataframe['Data Medicao'].dt.to_period("M"))[column].mean()
        
        # Getting year mean
        annual_mean = self.dataframe[column].mean()
        monthly_means['Year'] = annual_mean
        
        # Converting series to array
        monthly_means_array = monthly_means.values
        
        return monthly_means_array


    def convert_df(self):
        months = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
                        'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez', 'Year']
        new_df = pd.DataFrame()
        new_df['MÊS'] = months
        
        # Adiciona as médias mensais ao novo DataFrame
        for column in self.columns[1:]:
            new_df[column] = self.__get_mean(column)

        self.new_dataframe = new_df
        print('Successfully created a new dataframe!')

    def save_df(self):
        output_path = os.path.join(this_path, "../../../data/processed/csv/INMET/teste.csv")
        # Check if the data was treated
        if hasattr(self, 'new_dataframe'):
            self.new_dataframe.to_csv(output_path, index=False)
            print(f'Successfully saved the new dataframe to {output_path} as CSV.')
        else:
            print('Error: No new dataframe found. Run create_new_df first.')


    