import streamlit as st

def description():

    ttower_main_page = 'https://talltowers.bsc.es/'
    ttower_dowload_page = 'https://talltowers.bsc.es/access-the-data'

    st.title('Tower2csv API')

    st.write('By Marcos da Silva [(Linkedin)](%s)' %'https://www.linkedin.com/in/marcosp-araujo/')

    st.write('The Tower2csv is a Python-based API aimed at accessing global wind energy measurement data with ease. Its user-friendly interface (built with Streamlit) provides the downloading of data from the [Tall Tower Dataset](%s) in CSV format with only three clicks. This API automatically performs the following tasks:' % ttower_dowload_page)

    st.write('''
             - Request a dataset to the Tall Tower
             - Unzip the netCDF files 
             - Read and concatenate all netCDF files
             - Deliver the dataset in a single CSV file for downloading
             ''')
