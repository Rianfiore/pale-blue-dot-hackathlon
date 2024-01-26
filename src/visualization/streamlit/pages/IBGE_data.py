from src.data.entities.AgriculturalEstablishmentsData import AgriculturalEstablishmentsData
from src.data.entities.AgriculturalProductionData import AgriculturalProductionData

agricultural_production = AgriculturalProductionData().get_dict()
agricultural_establishments = AgriculturalEstablishmentsData().get_dict()

