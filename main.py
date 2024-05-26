'''
Main script example on how to use the Tower2csv.py

https://github.com/marcosp-araujo/Tower2csv/
'''

#%% 
from Tower2csv import Tower2csv

netcdf_dir = "./owez/10minutely/" # directory of the netCDF files
save_dir = "./"                   # directory to save the .csv file
save_file_name = "owez"           # year to be converted

T = Tower2csv(netcdf_dir, save_dir, save_file_name)
