import streamlit as st   

st.set_page_config(
    page_title="BeeInsightful Analytics",
    page_icon="bee",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)


text_about = "The Brazilian Data Bees' project aims to address crucial challenges in Brazil's agricultural sector by presenting a dynamic visual that empowers policymakers to make informed decisions. The visual combines vital datasets, including harvest yields, NASA's NDVI data, and Copernicus Soil Water Index, to provide a comprehensive overview of each state's agricultural conditions. Aligned with Sustainable Development Goals (SDGs), particularly zero hunger and climate action, the project seeks to optimize government resource distribution for farmer's financial support and sustainable food production. Utilizing reliable datasets from entities like IBGE, INMET, NASA, and ESA, the we foster a transparent, open science approach to empower policymakers aiming to contribute to a resilient and equitable agricultural landscape and tackle Brazil hunger problem."

st.title(":bar_chart: About the project")
st.markdown("##")

st.markdown("""---""")

st.write(text_about)

text_ndvi = "Explain the nvdi"
st.markdown("🌱**Normalized Difference Vegetation Index Dashboard**")
st.write(text_ndvi)