"""
@author: Marcos P. Araujo da Silva
https://github.com/marcosp-araujo/Tower2csv/

This code converts netCDF files from the Tall Tower database into a .CSV file
The data are provided by the Barcelona Super Computer Tall Tower Database:
https://talltowers.bsc.es/access-the-data

Required libraries:
xarray, netCDF4, pandas and numpy:

pip install xarray[all]
pip install netCDF4
pip install pandas
pip install numpy

"""

import os
import glob
import xarray as xr # library to read netCDF files
import pandas as pd
import numpy as np

###################################################################################

class Tower2csv:
    def __init__(self, netcdf_dir: str, save_dir: str, save_file:str): 
        ''' Constructor '''
        self.netcdf_dir = netcdf_dir # Directory of netCDF files
        self.save_dir = save_dir     # Directory to save the .csv
        self.save_file = save_file   # Name of the .csv file to be saved
        self.find_nc()               # find, read and convert netCDF files
        self.save_csv()              # save data in .csv
        
    def find_nc(self): ############################################
        '''This method scans the netCDF files in each sensor folder and join them
           into a single dataframe that is saved in CSV format.
        '''
        
      # Loop over sensors' folders
        df_all_files = pd.DataFrame() # To store all files
        folder_names = os.listdir(self.netcdf_dir) # Names of the sensors
        for current_folder in folder_names:
            print('Reading', current_folder, 'files')
            files_names = glob.glob(f"{self.netcdf_dir}/{current_folder}/*.nc")
          # Loop over netCDF files in the current sensor folder 
            df_concat_folder = pd.DataFrame()
            for current_file in files_names:
                df = self.nc2df(current_file)  # Converts netCDF into pandas dataframe
                df_concat_folder = pd.concat([df_concat_folder, df], axis = 0)
            df_all_files = pd.concat([df_all_files, df_concat_folder], axis = 1)   
             
        self.folder_names = folder_names     
        self.files_names = files_names           
        self.df_all_files = df_all_files
        self.df_concat_folder = df_concat_folder
        
    def nc2df(self, file:str): ##################################
        ''' This method reads and converts netCDF into a pandas dataframe '''
        nc = xr.open_dataset(file) # Reading the netcdf file
        df = nc.to_dataframe()     # Converting netcdf into dataframe
        df = df.droplevel(['latitude','longitude','height']) 
        # Keeps only the quality-assured data
        sensor = df.columns[0]; # Column of the quality-assured data (the other
        df = df[[sensor]]       # columns are 'quality_flag' or 'raw_data')
        df[( df <= -99999)] = np.nan   # NaN to values equals to -99999
        df.index = df.index.round("S") # Rounding milisecond to second
        return df
    
    def save_csv(self): ###########################################
        ''' This method saves the dataframe in .CSV format '''
        cvs_file_name = f"{self.save_dir}/{self.save_file}.csv"
        print(f'Saving data at: {cvs_file_name} \nPLEASE WAIT.')
      # Saving dataframe in CSV
        self.df_all_files.to_csv(cvs_file_name, sep = ',', decimal = '.') 
        print('The .CSV file has been saved.')  
        
###############################################################################
