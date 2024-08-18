import streamlit as st
import json

def tower_selector():
    f = open(".\\app_modules\\tower_names.json",'r')
    tower_names = json.load(f)['tower_names']
    tower_name = st.selectbox('Select a meteorological tower and click in "Start processing"', tower_names)
    start_processing = st.button('Start processing')

    return tower_name, start_processing