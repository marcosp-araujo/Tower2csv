''' This is the main script of the streamlit-based app
    Author: Marcos
'''

import streamlit as st
from tower2csv.Tower2csv import Tower2csv
from app_modules.description import description
from app_modules.tower_selector import tower_selector
from app_modules.download import download

if __name__ == '__main__':

    description()
    tower_name, start_process = tower_selector()

    if (tower_name != '') and (start_process is True):
        st.write('Processing... Please, wait for the download button:')
        with st.empty():
            T = Tower2csv(tower_name = tower_name, 
                          unzip_dir = './Data',
                          remove_unzip_files = True)
        if T.df_all_files.isna().all().all() is True:
            st.write('All data found are NaN. Please, try another tower.')
        download(T)
 