''' This is the main script of the streamlit-based app
    Author: Marcos
'''

import streamlit as st
from tower2csv.Tower2csv import Tower2csv
from app_modules.tower_selector import tower_selector
from app_modules.download import download

if __name__ == '__main__':
    st.title('Tower2csv API')

    ttower_link = 'https://talltowers.bsc.es/access-the-data'
    st.write('The Tower2csv processes raw data from the Tall Tower database and provides filtered data in a single .CSV. It automatically connects to the Tall Tower via API. Details about the available meteorological towers can be found in the [Tall Tower download page](%s), where the data are shared via netCDF files compressed in .ZIP.' % ttower_link)

    tower_name, start_process = tower_selector()

    if (tower_name is not '') and (start_process is True):
        st.write('Processing... Please, wait')
        st.write('A download button will show up once the process is finished')
        with st.empty():
            T = Tower2csv(tower_name = tower_name, 
                          unzip_dir = r'.\\Data_tmp',
                          remove_unzip_files = True)
        download(T)
 