
"""
@author: Marcos P. Araujo
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
import numpy as np
from auxiliar.data_API import data_API
from app_modules.streamlit_log_messages import streamlit_log_messages

# ----------------------------------------------------------------------- #
class Tower2csv:
    tower_name: str             # Site name
    unzip_dir: str              # Directory to extract the netCDF files
    save_file_path: str = None  # Path of the .csv file to be saved
    run: classmethod            # Starts the processing chain
    unzip: classmethod          # Extract netCDF files
    find_paths: classmethod     # Gather netCDF files paths
    read_nc: classmethod        # read netCDF files
    save_csv: classmethod       # Save output as a .csv file
    df_all_files: pd.DataFrame  # Data from all netCDF files
    # -------------------------------------------------------------------- # 
    def __init__(self, 
                 tower_name, 
                 unzip_dir, 
                 save_file_path = None,
                 remove_unzip_files = False): 
      ''' Constructor '''
      self.tower_name = tower_name.lower().replace(' ','_')
      self.unzip_dir = unzip_dir
      self.save_file_path = save_file_path
      self.remove_unzip_files = remove_unzip_files
      self.run()
    # -------------------------------------------------------------------- #  
    def run(self) -> None:
      ''' This method runs all processing steps '''
      if self.tower_name is not None: 
        self.unzip()
        self.find_paths()
        self.read_nc() 
        self.remove_unzip_folder()        
        self.save_csv() 
    # -------------------------------------------------------------------- # 
    def unzip(self) -> None:
      ''' Extract files from .zip '''
      self.zip_path = data_API(self.tower_name)
      os.makedirs(self.unzip_dir,  exist_ok=True)
      with zipfile.ZipFile(self.zip_path, 'r') as zip_file:
        zip_file.extractall(f"{self.unzip_dir}")
    # -------------------------------------------------------------------- # 
    def find_paths(self) -> None:
      ''' This method finds all sensor folders inside the tower folder '''
      path_pattern = os.path.join(self.unzip_dir, self.tower_name, "*", "*")
      self.folder_names = glob.glob(path_pattern)
    # -------------------------------------------------------------------- #  
    def read_nc(self) -> None: 
      '''This method scans the netCDF files in each sensor folder and join them
          into a single dataframe that is saved in CSV format.
      '''
      # Loop over sensors' folders
      df_all_files = pd.DataFrame() # To store all files
      N_folders = len(self.folder_names)
      log_messages = []
      for count, current_folder in enumerate(self.folder_names):
        current_folder = os.path.normpath(current_folder)
        sensor_name = os.path.basename(current_folder)
        count += 1
        message = f'Processing {sensor_name} (folder {count}/{N_folders})'
        log_messages.append(message)

        streamlit_log_messages(log_messages)
        print(message)
        file_paths_patern = os.path.join(current_folder,"*.nc")
        files_list = glob.glob(file_paths_patern)
        # xr.concat is faster than "xr.open_mfdataset"
        nc = xr.concat([xr.open_dataset(i) 
                        for i in files_list], dim = "time")
        df_folder = self.nc2df(sensor_name, nc)
        if df_folder.isna().all() is True:
          print('  All data in this folder are NaN') 
          continue
        else:
          df_folder = df_folder.reset_index()
          df_folder = df_folder.drop_duplicates(subset='time').set_index('time')
          df_all_files = pd.concat([df_folder, df_all_files], axis = 1)

      # Storing results in  the object  
      self.df_all_files = df_all_files   
      self.df_folder = df_folder
    # -------------------------------------------------------------------- #        
    def nc2df(_, sensor_name, nc) -> pd.DataFrame: 
      ''' This method reads and converts a netCDF into a pandas dataframe '''
      df = nc.to_dataframe()         # Converting netcdf into dataframe
      df = df.droplevel(['height','longitude', 'latitude'])  # Height info is the column name
      #df = df.reset_index(level = ('longitude', 'latitude'))
      df = df[[sensor_name]]         # quality-assured column
      df.index = df.index.round("s") # Rounding milisecond to second
      df = df.replace([-9999,'NaN','nan'], np.nan)
      return df
    # -------------------------------------------------------------------- # 
    def remove_unzip_folder(self) -> None:
      ''' This method removes the unzip folder '''
      if self.remove_unzip_files is True:
        try:
          shutil.rmtree(self.unzip_dir)
        except:
          pass
    # -------------------------------------------------------------------- #     
    def save_csv(self) -> None: 
      ''' This method saves the dataframe in .CSV format '''
      if self.save_file_path is not None:
        self.save_file_path = os.path.normpath(self.save_file_path)
        cvs_file_name = f"{self.save_file_path}.csv"
        print(f'Saving data at: {cvs_file_name} \nPLEASE WAIT.')
        self.df_all_files.to_csv(cvs_file_name, sep = ',', decimal = '.') 
        print('The .CSV file has been saved.')  
# ----------------------------------------------------------------------- #
