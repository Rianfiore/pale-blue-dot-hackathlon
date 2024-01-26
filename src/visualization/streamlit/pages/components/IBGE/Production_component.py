from src.data.entities.AgriculturalProductionData import AgriculturalProductionData
from src.data.entities.AgriculturalProductionData import AgriculturalColumns
from src.data.entities.AgriculturalProductionData import MonthColumns
from src.data.entities.AgriculturalProductionData import FederationColumns

import streamlit as st

class IbgeProductionComponent:
  def __init__(self):
    self.agricultural_production = AgriculturalProductionData().get_dict()
    
  def render(self):
    # Create title and display it
    st.title('Production')
    
    # Create selectbox for each filter    
    agricultural_type = st.selectbox('Select the type of production', options=AgriculturalColumns)
    month_reference = st.selectbox('Select the month reference', options=MonthColumns)
    state = st.selectbox('Select the state', options=FederationColumns)
    
    # Create the dataframe and display it with filters
    st.dataframe(self.agricultural_production[agricultural_type][month_reference][state], use_container_width=True)
  