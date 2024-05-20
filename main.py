# Main script example of how to use the Tower2csv
# version 1.0

import os
from Tower2csv import Tower2csv

netcdf_dir = './owez/10minutely/' # directory of the netcdf files
year = 2009     # year to be converted
save_dir = os.getcwd()  # directory to save the .csv files

T = Tower2csv(netcdf_dir,year,save_dir)
