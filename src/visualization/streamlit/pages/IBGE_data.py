from src.visualization.streamlit.pages.components.IBGE.Establishments_component import IbgeEstablishmentsComponent
from src.visualization.streamlit.pages.components.IBGE.Production_component import IbgeProductionComponent
import streamlit as st

ibge_production_component = IbgeProductionComponent()
ibge_establishments_component = IbgeEstablishmentsComponent()

st.sidebar.header('Please Filter Here:')

dataType = st.sidebar.multiselect(
   'Select the data type',
   options=['Agricultural Production', 'Agricultural Establishments'],
   default={'Agricultural Establishments'}
)

st.title(":bar_chart: Agricultural Data Dashboard")
st.markdown("##")


if 'Agricultural Production' in dataType:
  ibge_production_component.render()
if 'Agricultural Establishments' in dataType:
  ibge_establishments_component.render()
  
