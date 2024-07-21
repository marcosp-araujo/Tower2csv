"""
@author: Marcos P. Araujo da Silva
https://github.com/marcosp-araujo/Tower2csv/

This code converts netCDF files from the Tall Tower database into a .CSV file
The data are provided by the Barcelona Super Computer Tall Tower Database:
https://talltowers.bsc.es/access-the-data

Required libraries: see "requirements.txt":

"""

import os
import glob
import xarray as xr # library to read netCDF files
import pandas as pd

# ----------------------------------------------------------------------- #
class Tower2csv:
    netcdf_dir = str      # Directory of netCDF files
    save_file_path = str  # Path of the .csv file to be saved
    find_nc = classmethod # finds, reads and converts netCDF files
    find_nc = classmethod # save data in .csv
    df_all_files = pd.DataFrame # Data from all netCDF files
# ----------------------------------------------------------------------- # 
    def __init__(self, netcdf_dir: str, save_file_path:str): 
      ''' Constructor '''
      self.netcdf_dir = netcdf_dir 
      self.save_file_path = save_file_path 
      self.find_nc()               
      self.save_csv()              
# ----------------------------------------------------------------------- #       
    def find_nc(self): 
      '''This method scans the netCDF files in each sensor folder and join them
          into a single dataframe that is saved in CSV format.
      '''
      # Loop over sensors' folders
      df_all_files = pd.DataFrame() # To store all files
      folder_names = os.listdir(self.netcdf_dir) # Names of the sensors
      for current_folder in folder_names:
          print('Reading', current_folder, 'folder')
          files_names = glob.glob(f"{self.netcdf_dir}/{current_folder}/*.nc")
          # Loop over netCDF files in the current sensor folder 
          df_concat_folder = pd.DataFrame()
          for current_file in files_names:
              df = self.nc2df(current_file)  # Converts netCDF into pandas dataframe
              df_concat_folder = pd.concat([df_concat_folder, df], axis = 0)
          df_all_files = pd.concat([df_all_files, df_concat_folder], axis = 1)

      # Dropping duplicated "latitude" and "logitude" columns
      df_all_files = df_all_files.T.drop_duplicates().T 

      # Storing results in  the object  
      self.df_all_files = df_all_files   
      self.folder_names = folder_names     
      self.files_names = files_names           
      self.df_concat_folder = df_concat_folder
# ----------------------------------------------------------------------- #      
    def nc2df(self, file:str): 
      ''' This method reads and converts a netCDF into a pandas dataframe '''
      nc = xr.open_dataset(file) # Reading the netcdf file
      df = nc.to_dataframe()     # Converting netcdf into dataframe
      df = df.droplevel(['height']) # Height info is the column name
      df = df.reset_index(level = ('longitude', 'latitude'))
      df = df.iloc[:, 0:3] # 'longitude', 'latitude', and quality-assured column
      df[( df <= -9999)] = pd.NA   # NaN to values equals to -99999
      df.index = df.index.round("S") # Rounding milisecond to second
      return df
# ----------------------------------------------------------------------- #    
    def save_csv(self): 
      ''' This method saves the dataframe in .CSV format '''
      cvs_file_name = f"{self.save_file_path}.csv"
      print(f'Saving data at: {cvs_file_name} \nPLEASE WAIT.')
      self.df_all_files.to_csv(cvs_file_name, sep = ',', decimal = '.') 
      print('The .CSV file has been saved.')  
# ----------------------------------------------------------------------- # 
