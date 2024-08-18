
"""
@author: Marcos P. Araujo da Silva
https://github.com/marcosp-araujo/Tower2csv/

This code converts netCDF files from the Tall Tower database into a .CSV file
The data are provided by the Barcelona Super Computer Tall Tower Database:
https://talltowers.bsc.es/access-the-data

Required libraries: see "requirements.txt":

"""
import shutil
import zipfile
import os
import glob
import streamlit as st
import xarray as xr 
import pandas as pd
from tower2csv.data_API import data_API

# ----------------------------------------------------------------------- #
class Tower2csv:
    tower_name: str      # Site name
    unzip_dir: str       # Directory to extract the netCDF files
    save_file_path: str  # Path of the .csv file to be saved

    run: classmethod        # Starts the processing chain
    unzip: classmethod      # Extract netCDF files
    find_paths: classmethod # Gather netCDF files paths
    read_nc: classmethod    # read netCDF files
    save_csv: classmethod   # Save output as a .csv file
    
    df_all_files: pd.DataFrame # Data from all netCDF files
# ----------------------------------------------------------------------- # 
    def __init__(self, 
                 tower_name = None, 
                 unzip_dir = None, 
                 save_file_path = None,
                 remove_unzip_files = False): 
      ''' Constructor '''
      self.tower_name = tower_name 
      self.unzip_dir = f"{unzip_dir}\\{tower_name}"
      self.save_file_path = save_file_path
      self.remove_unzip_files = remove_unzip_files
      self.run()
# ----------------------------------------------------------------------- # 
    def run(self):
      if self.tower_name is not None: 
        self.unzip()
        self.find_paths()
        self.read_nc() 
        self.remove_unzip_folder()        
        self.save_csv() 
# ----------------------------------------------------------------------- # 
    def unzip(self):
      ''' Extract files from .zip '''
      self.zip_path = data_API(self.tower_name)
      if os.path.isdir(self.unzip_dir) is False:
        os.mkdir(self.unzip_dir)
      with zipfile.ZipFile(self.zip_path, 'r') as zip_file:
        zip_file.extractall(f"{self.unzip_dir}")
# ----------------------------------------------------------------------- #
    def find_paths(self):
      self.folder_names = glob.glob(f"{self.unzip_dir}\\*\\*\\*\\")
      self.tower_name = glob.glob(f"{self.unzip_dir}\\*")[0].split("\\")[-1]
# ----------------------------------------------------------------------- #
    def read_nc(self): 
      '''This method scans the netCDF files in each sensor folder and join them
          into a single dataframe that is saved in CSV format.
      '''
      # Loop over sensors' folders
      df_all_files = pd.DataFrame() # To store all files
      N_folders = len(self.folder_names)
      for count, current_folder in enumerate(self.folder_names):
        sensor_name = current_folder.split("\\")[-2]
        count += 1
        message = f'Processing {sensor_name} (folder {count}/{N_folders})'
        st.write(message)
        print(message)
        files_list = glob.glob(f"{current_folder}\\*.nc")
        nc = xr.concat([xr.open_dataset(i) 
                        for i in files_list], dim = "time")
        df_folder = self.nc2df(sensor_name, nc)
        df_all_files = pd.concat([df_folder, df_all_files], axis = 1)

      # Storing results in  the object  
      self.df_all_files = df_all_files   
      self.df_folder = df_folder
# ----------------------------------------------------------------------- #      
    def nc2df(_, sensor_name, nc): 
      ''' This method reads and converts a netCDF into a pandas dataframe '''
      df = nc.to_dataframe()         # Converting netcdf into dataframe
      df = df.droplevel(['height','longitude', 'latitude'])  # Height info is the column name
      #df = df.reset_index(level = ('longitude', 'latitude'))
      df = df[[sensor_name]]         # quality-assured column
      df.index = df.index.round("s") # Rounding milisecond to second
      df[( df <= -9999)] = pd.NA     # NaN to values equals to -99999
      return df
# ----------------------------------------------------------------------- #
    def remove_unzip_folder(self):
      if self.remove_unzip_files is True:
        try:
          shutil.rmtree(self.unzip_dir)
        except:
          pass
# ----------------------------------------------------------------------- #    
    def save_csv(self): 
      ''' This method saves the dataframe in .CSV format '''
      if self.save_file_path is not None:
        cvs_file_name = f"{self.save_file_path}.csv"
        print(f'Saving data at: {cvs_file_name} \nPLEASE WAIT.')
        self.df_all_files.to_csv(cvs_file_name, sep = ',', decimal = '.') 
        print('The .CSV file has been saved.')  
# ----------------------------------------------------------------------- #