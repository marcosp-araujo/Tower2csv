"""
@author: Marcos P. Araujo da Silva

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
    def __init__(self, netcdf_dir, save_dir, save_file):
        ''' Constructor '''
        self.netcdf_dir = netcdf_dir # Directory of netCDF files
        self.save_dir = save_dir     # Directory to save the .csv
        self.save_file = save_file   # Name of the .csv file to be saved
        self.find_nc()               # find, read and convert netCDF files
        self.save_csv()              # save data in .csv
        
    def find_nc(self): ############################################################
        '''This method scans the netCDF files in each sensor folder and join them
           into a single dataframe that is saved in CSV format.
        '''
        df_concat = pd.DataFrame()
        df_year = pd.DataFrame()
      # Loop over sensors' folders
        sensors_folders = os.listdir(self.netcdf_dir) # Names of the sensors
        for sensor_dir in sensors_folders:
            print('Reading', sensor_dir, 'files')
            files_names = glob.glob(f"{self.netcdf_dir}/{sensor_dir}/*.nc")
          # Loop over netCDF files in the current sensor folder 
            for current_file in files_names:
                df = self.nc2df(current_file)  # Calling the conversor method
                df_concat = pd.concat([df_concat, df])
            df_year = pd.concat([df_year, df_concat], axis = 1)
            df_concat = pd.DataFrame()     
             
        self.sensors_folders = sensors_folders     
        self.files_names = files_names           
        self.df_year = df_year
        self.df_concat = df_concat
        
    def nc2df(self,file): ######################################################
        ''' This method reads and converts netcdf into dataframe  
        '''
        nc = xr.open_dataset(file) # Reading the netcdf file
        df = nc.to_dataframe()     # Converting netcdf into dataframe
        df = df.droplevel(['latitude','longitude','height']) 
        # Keep only the quality-assured data
        sensor = df.columns[0]; # Column of the quality-assured data
        df = df[[sensor]]       # (the other columns are 'quality_flag' or 'raw_data')
        df[( df < -9999)] = np.nan # NaN to values equals to -99999
        df.index = df.index.round("S") # Rounding the milisecond
        return df
    
    def save_csv(self): ########################################################
        ''' This method saves the dataframe in .csv format '''
        cvs_file_name = f"{self.save_dir}/{self.save_file}.csv"
        print('Saving the ', cvs_file_name,' file \n PLEASE WAIT.')
      # Saving dataframe in csv
        self.df_year.to_csv(cvs_file_name, sep = ',', decimal = '.') 
        print('The .csv file has been saved.')  
        
###############################################################################
