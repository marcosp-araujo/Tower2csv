# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 06:55:16 2023

@author: Marcos P. Araujo da Silva

This code converts netcdf files from the Tall Tower database into csv files
The data was provided by the Barcelona Super Computer Tall Tower Database:
https://talltowers.bsc.es/access-the-data.


THIS SCRIPT REQUIRES THE xarray LIBRARY. SEE INSTALLATION INSTRUCTIONS BELOW:
https://docs.xarray.dev/en/stable/getting-started-guide/installing.html#installation-instructions

"""

import os
import xarray as xr # library to read netcdf files
import pandas as pd
import numpy as np

#%% ###########################################################################

class Tower2csv:
    def __init__(self,netcdf_dir,year,save_dir):
        self.netcdf_dir = netcdf_dir # Directory of netcdf files
        self.year = str(year) # Year of data to be joined and converted
        self.save_dir = save_dir # Directory to save the .csv
        self.find_nc()  # find, read and convert netcdf files
        self.save_csv() # save data in .csv
        
###############################################################################
## This method scans the netcdf files and calls the converter method
## It joins all data from a given year into a one single dataframe
    def find_nc(self):
        files_dir = list() # Full directories of the netcdf files
        files_names = list() # To receive only files names
        sensors_names = list() # Names of the sensors
        df_concat = pd.DataFrame()
        df_year = pd.DataFrame()
        for sensor_dir in os.listdir(self.netcdf_dir):
            print('Reading', sensor_dir,'files')
          # Current directory
            current_dir = (os.path.join(self.netcdf_dir, sensor_dir))
            for current_file in os.listdir(current_dir):
                if current_file.find(self.year) >= 0:
                    files_dir.append(os.path.join(current_dir, current_file))
                    files_names.append(current_file)
                    sensors_names.append(current_file.split('_')[0]) 
                  #print(files_dir[-1])
                  # Calling coverted method
                    df = self.nc2df(files_dir[-1])
                    df_concat = pd.concat([df_concat,df])
            df_year = pd.concat([df_year,df_concat],axis = 1)
            df_concat = pd.DataFrame()     
             
        self.sensors_names = np.unique(sensors_names)     
        self.files_dir = files_dir
        self.files_names = files_names           
        self.df_year = df_year
        self.df_concat = df_concat
        
###############################################################################  
## This method reads and converts netcdf into dataframe       
    def nc2df(self,file):
        nc = xr.open_dataset(file) #Reading the netcdf file
        df = nc.to_dataframe()     #Converting netcdf into dataframe
       #Dropping "latitude", "longitude" and "height" indexes
        df = df.droplevel(['latitude','longitude','height']) 
        sensor = df.columns[0]; #It is the main quality-assured column 
      # Omiting the milisecond information
        df.index = df.index.round("S")
      # Keep only the quality-assured main current_sensor 
      # (the others are 'quality_flag' or 'raw_data')
        df = df[[sensor]]
        df.columns
      # Asignin NaN to values equals to -99999
        df[sensor] [( df[sensor] < -9999)] = np.nan
        return df
    
###############################################################################
## This method saves the dataframe in .csv format
    def save_csv(self):
        cvs_file_dir = self.save_dir  + "/" + self.year + ".csv"
        print('Saving .csv file:',cvs_file_dir,'\n PLEASE WAIT.')
      # Saving dataframe in csv
        self.df_year.to_csv(cvs_file_dir, sep = ',', decimal = '.') 
        print('The .csv file has been saved.')  
        
###############################################################################
