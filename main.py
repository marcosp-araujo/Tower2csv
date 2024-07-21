'''
Main script example on how to use the Tower2csv.py

https://github.com/marcosp-araujo/Tower2csv/
'''

#%% 

from modules.Tower2csv import Tower2csv

if __name__ == "__main__":

    netcdf_dir = r".\Data\owez\10minutely" # directory of the netCDF files
    save_file_path = r".\Data\owez"        # Path to save the .csv file

    T = Tower2csv(netcdf_dir, save_file_path)
