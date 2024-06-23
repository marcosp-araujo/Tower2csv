'''
Main script example on how to use the Tower2csv.py

https://github.com/marcosp-araujo/Tower2csv/
'''

#%% 

from modules.Tower2csv import Tower2csv

if __name__ == "__main__":
    netcdf_dir = r".\owez\10minutely" # directory of the netCDF files
    save_dir = "."                    # directory to save the .csv file
    save_file_name = "owez"           # Save file name

    T = Tower2csv(netcdf_dir, save_dir, save_file_name)

# %%
