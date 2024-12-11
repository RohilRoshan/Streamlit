import streamlit as st
import pandas as pd

st.title("Choose a Data(CSV) File")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("###Data Preview")
    st.dataframe(df)
    st.line_chart(df)

    st.write("### Summary Stats")
    st.write(df.describe())