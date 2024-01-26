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

text_ndvi = "The Normalized Difference Vegetation Index (NDVI) is an indicator of the greenness of the biomes. Even though it is not a physical property of the vegetation cover, its very simple formulation NDVI = (REF_nir – REF_red)/(REF_nir + REF_red) where REF_nir and REF_red are the spectral reflectances measured in the near infrared and red wavebands respectively, makes it widely used for ecosystems monitoring."
st.markdown("🌱**Normalized Difference Vegetation Index Dashboard**")
st.write(text_ndvi)

text_cswi = "The Soil Water Index quantifies the moisture condition at various depths in the soil. It is mainly driven by the precipitation via the process of infiltration. Soil moisture is a very heterogeneous variable and varies on small scales with soil properties and drainage patterns. Satellite measurements integrate over relative large-scale areas, with the presence of vegetation adding complexity to the interpretation."
st.markdown("🌱**Copernicus Soil Water Index Dashboard**")
st.write(text_cswi)