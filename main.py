'''
Main script example on how to use the Tower2csv.py via terminal

https://github.com/marcosp-araujo/Tower2csv/
'''

#%% 

from tower2csv.Tower2csv import Tower2csv

if __name__ == "__main__":

    site = '42361' # Tower name
    unzip_dir = r".\\Data_tmp" # Directory to extract the netCDF files
    save_file_path = f".\\Data\\{site}" # Path to save the .csv file
    T = Tower2csv(site, unzip_dir, save_file_path)
