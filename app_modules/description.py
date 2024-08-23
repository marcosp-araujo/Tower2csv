import streamlit as st

def description():

    ttower_main_page = 'https://talltowers.bsc.es/'
    ttower_dowload_page = 'https://talltowers.bsc.es/access-the-data'

    st.title('Tower2csv API')
    
    st.write('By Marcos da Silva [(Linkedin)](%s)' %'https://www.linkedin.com/in/marcosp-araujo/')

    st.write('The Tower2csv is a Python-based API aimed at accessing global wind energy measurement data with ease. Its user-friendly interface (built with Streamlit) provides the downloading of data from the [Tall Tower Dataset](%s) with only three clicks. This API automatically performs the following tasks:' % ttower_main_page)

    st.markdown('- Requests a dataset to the Tall Tower')
    st.markdown('- Unzip the netCDF files')
    st.markdown('- Reads and concatenates all netCDF files')
    st.markdown('- Delivers the output dataset in a single .CSV for downloading')
    st.write('Detailed information on the available meteorological towers can be found at the [Tall Tower download page](%s)' % ttower_dowload_page)
