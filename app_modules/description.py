import streamlit as st

def description():
    st.title('Tower2csv API')
    ttower_main_page = 'https://talltowers.bsc.es/'
    ttower_dowload_page = 'https://talltowers.bsc.es/access-the-data'
    st.write('The Tower2csv API simplifies the access to the [Tall Tower](%s) Dataset  by  performing the following tasks:' % ttower_main_page)
    st.markdown('- Automatically requests a dataset to the Tall Tower')
    st.markdown('- Unzip the netCDF files')
    st.markdown('- Reads and concatenates all netCDF files')
    st.markdown('- Delivers the output dataset in a single .CSV for downloading')
    st.write('Detailed information on the available meteorological towers can be found at the [Tall Tower download page](%s)' % ttower_dowload_page)