'''
Main script example on how to use the Tower2csv.py
'''

#%% 
import os
from Tower2csv import Tower2csv
from Tower2csv_2 import Tower2csv_2

netcdf_dir = './owez/10minutely/' # directory of the netCDF files
save_dir = os.getcwd()  # directory to save the .csv file
save_file_name = "owez" # year to be converted

T = Tower2csv_2(netcdf_dir, save_dir, save_file_name)
