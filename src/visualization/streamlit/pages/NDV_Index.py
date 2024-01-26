import pandas as pd
import streamlit as st
import os



st.set_page_config(
    page_title="Green Area",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)


folder_path = os.path.join(os.path.dirname(__file__), "../../../../data/raw/csv/NASA/ndvi/ndvi_data.csv")
PERCENT = 100

df = pd.read_csv(folder_path, sep = ';', index_col=0)

df =  (df * PERCENT).astype(str) + '%'              

df.index = [str.upper(index) for index in df.index]
df.columns = [str.capitalize(columns) for columns in df.columns]


st.sidebar.header("Please Filter Here:")
state = st.sidebar.multiselect(
  "Select the State",
  options=df.index.unique(),
  default=df.index.all() 
)

df_selection = df.query(
    "index == @state "
)

st.title(":bar_chart: Normalized Difference Vegetation Index Dashboard")
st.markdown("##")

# Check if the dataframe is empty:
if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop() # This will halt the app from further execution.


st.line_chart(df_selection.transpose())        

st.dataframe(df_selection)    