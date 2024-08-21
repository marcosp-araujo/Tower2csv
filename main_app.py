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

    if (tower_name is not '') and (start_process is True):
        st.write('Processing... Please, wait')
        st.write('A download button will show up once the process is finished')
        with st.empty():
            T = Tower2csv(tower_name = tower_name, 
                          unzip_dir = r'.//Data_tmp',
                          remove_unzip_files = True)
        download(T)
 