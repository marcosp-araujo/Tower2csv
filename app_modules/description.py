import streamlit as st

def description():
    st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.title('Tower2csv API')

    st.write('By Marcos da Silva [(Linkedin)](%s), on April 6, 2025.' %'https://www.linkedin.com/in/marcosp-araujo/')

    st.markdown("""
    <p style='text-align: justify;'>
        The Tower2csv is aimed at accessing global wind energy measurement data from the
        <a href={'https://talltowers.bsc.es/access-the-data'} target='_blank'>Tall Tower Dataset</a>
        with ease. Its user-friendly interface enables downloading data from a meteorological
        tower in CSV format. This API automatically requests a dataset to the Tall Tower, unzips, reads and concatenates all netCDF files, and finally, delivers the dataset in a single CSV file.
    </p>
""", unsafe_allow_html=True)
    
    