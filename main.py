'''
Main script example on how to use the Tower2csv.py via terminal

https://github.com/marcosp-araujo/Tower2csv/
'''

#%% 

from tower2csv.Tower2csv import Tower2csv

if __name__ == "__main__":

    tower_name = 'Delvar'  # Tower name
    unzip_dir = r"./Data" # Directory to extract the netCDF files
    save_file_path = f"./Data/{tower_name}" # Path to save the .csv file
    T = Tower2csv(tower_name, unzip_dir, save_file_path)

