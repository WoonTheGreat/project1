import streamlit as st
import pandas as pd
import sweetviz as sv


st.set_page_config(
    page_title="LayZii Project 1",
    page_icon="random",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'About': "LayZii first project!"
    }
)

st.title('Data Exploring App')

# insert CSV file & reads as table
uploaded_file = st.file_uploader("Upload CSV file", type=['CSV'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
# usw sweetviz to analyze table & show report
    my_report = sv.analyze(df)
    my_report.show_html()
