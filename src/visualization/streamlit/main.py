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

text_IBGE_01 = "The IBGE conducted the Agricultural Census 2017 with the aim of portraying the reality of Agricultural Brazil, considering its interrelationships with actors, scenarios, modes, and instruments of action. Therefore, in order to achieve a better approximation that identified and captured the dynamics of productive means and land use, the variability in occupation and labor relations, the degree of specialization and technification of labor, the growing interest in the reflections on environmental heritage, and all the changes that have occurred since the last survey – the Agricultural Census 2006 – a resizing was applied to the data capture model, in terms of conceptual aspects, based on the premises suggested in the World Agricultural Census Program 2020, developed by the Food and Agriculture Organization (FAO) of the United Nations in 2016; the categorizations of the National Classification of Economic Activities – CNAE 2.0, elaborated by IBGE in 2007, and in accordance with the International Standard Industrial Classification of All Economic Activities – ISIC."
text_IBGE_02 = "Historical series of the annual estimate of planted area, harvested area, production, and average yield of crops."
st.markdown("🌱**Systematic Agricultural Production Survey and Agricultural Census**")
st.write(text_IBGE_02)
st.write(text_IBGE_01)