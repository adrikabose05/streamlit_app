import streamlit as st
import pandas as pd
st.set_page_config(
  page_title="Covid 19",
  layout="wide"
  initial_sidebar_state="expanded"
)

st.title("📁 Load Local Dataset")

df = pd.read_csv("data.csv")
st.write("Loaded Data:")
st.dataframe(df)

st.title("Covid 19 Dashboard")
st.write("")
