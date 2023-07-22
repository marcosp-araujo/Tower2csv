# Main code example of how to call the Tower2csv
# version 1.0

import os
from Tower2csv import Tower2csv

cwd = os.getcwd()
parent = os.path.dirname(cwd)
netcdf_dir = parent + '/owez/10minutely/' #directory of the netcdf files
year = "2006";           #year to be converted
save_dir = parent + '/owez/csv/' #directory to save the .csv files

T = Tower2csv(netcdf_dir,year,save_dir)
