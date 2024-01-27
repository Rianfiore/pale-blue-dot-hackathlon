from src.data.entities.AgriculturalProductionData import AgriculturalProductionData
from src.data.entities.AgriculturalEstablishmentsData import AgriculturalEstablishmentsData
from src.data.entities.InmetData import InmetData

# Creating INMET data and saving it
inmet_data = InmetData()

# Creating agricultural production data and saving it
agricultural_production = AgriculturalProductionData()
agricultural_production.save_df()

# Creating agricultural establishments data and saving it
agricultural_establishments = AgriculturalEstablishmentsData()
agricultural_establishments.save_df()