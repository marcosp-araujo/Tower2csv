''' The modules are used to get information within zip files
'''
import zipfile
from io import BytesIO
import xarray as xr

# ----------------------------------------------------------------------- # 
def read_zip(zip_path):
    ''' Get the .zip file and list of files within it'''
    zip_file = zipfile.ZipFile(zip_path,"r") # reading .ZIP file
    files_path = zip_file.namelist() # files paths within .ZIP
    return zip_file, files_path
# ----------------------------------------------------------------------- #  
def find_sensor(path):
    ''' Returns sensor's folder'''
    if ".nc" in path:
        return path.split("/")[2]
# ----------------------------------------------------------------------- #     
def read_nc_in_zip(zip_file, path):
    ''' Reads netCDF within a zip file'''
    if ".nc" in path:
        file = BytesIO(zip_file.read(path))
        nc = xr.open_dataset(file)
        return nc