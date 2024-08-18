import streamlit as st
from tower2csv.Tower2csv import Tower2csv

def download(T:Tower2csv):
    @st.cache_data
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv(
                         sep = ',', 
                         decimal = '.').encode("utf-8")

    csv = convert_df(T.df_all_files)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name=f"{T.tower_name}.csv",
        mime="text/csv",
    )