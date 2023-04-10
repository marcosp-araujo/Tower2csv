# Main code example of how to call the Tower2csv

import os
from Tower2csv import Tower2csv

netcdf_dir = os.getcwd() + '/owez/10minutely/'; #directory of the netcdf files
year = "2005";           #year that to be converted
save_dir = os.getcwd() + '/owez/csv/'; #directory to save the .csv files

C = Tower2csv(netcdf_dir,year,save_dir)