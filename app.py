import streamlit as st
import pandas as pd
st.set_page_config(
  page_title="Covid 19",
  layout="wide"
  initial_sidebar_state="expanded"
)
st.title("Covid 19 Dashboard")
df = pd.read_csv("covid_data(2).xlsx")
st.write("Loaded Data:")
st.dataframe(df)


st.write("")
