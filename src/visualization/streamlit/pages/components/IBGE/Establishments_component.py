from src.data.entities.AgriculturalEstablishmentsData import AgriculturalEstablishmentsData, FederationColumns, ProductColumns, TypologyColumns
import streamlit as st

class IbgeEstablishmentsComponent:
  def __init__(self):
    self.agricultural_establishments = AgriculturalEstablishmentsData().get_dict()
    
  def render(self):
      # Create title and display it
      st.title('Establishments')
    
          
      # Create selectbox for each filter    
      typology = st.selectbox('Select the Typology', options=TypologyColumns)
      state = st.selectbox('Select the State', options=FederationColumns)
      product = st.selectbox("Select the Product", options=ProductColumns)
    
      establishments_data = self.agricultural_establishments[typology][state][product]
      # Create the dataframe and display it with filters
      st.bar_chart(establishments_data, use_container_width=True)
      
   