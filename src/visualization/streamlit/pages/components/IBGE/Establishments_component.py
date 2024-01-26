from src.data.entities.AgriculturalEstablishmentsData import AgriculturalEstablishmentsData
import streamlit as st

class IbgeEstablishmentsComponent:
  def __init__(self):
    self.agricultural_establishments = AgriculturalEstablishmentsData().get_dict()
    
  def render(self):
        # Create title and display it
        st.title('Establishments')
        
        # Create DataFrame and display it
        st.dataframe(self.agricultural_establishments)
  