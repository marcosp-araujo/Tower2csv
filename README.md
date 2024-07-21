### Introduction

  The Tall Tower is an open database aimed at boosting the use of hub-height wind observations from meteorological towers.
  The [Tower2csv.py](/modules/Tower2csv.py) class scans netCDF files from a Tall Tower database and joins all of them into a single .CSV file. 

### Requirements and virtual environment

Creating a virtual environment is strongly advisable to avoid errors when running the Tower2csv. It can be done using the "virtualenv" library. Use the following command lines in your terminal:

```
pip install virtualenv
```
To create a new virtual environment called "venv":
```
python -m venv venv
```

Now, activate the new virtual environment:
```
.\venv\Scripts\activate
```

Then, install the [requirements.txt](requirements.txt):

```
pip install -r requirements.txt
````

### How to use

In the [main.py](/main.py) script you can set the netCDF files directory and the name of the output .csv file. Example data can be found in the [owez](Data/owez) folder.
```
from modules.Tower2csv import Tower2csv

if __name__ == "__main__":
   
    netcdf_dir = r".\owez\10minutely" # directory of the netCDF files
    save_file_path = r".\owez"        # directory to save the .csv file

    T = Tower2csv(netcdf_dir, save_file_path)
```

Once the new environment is activated, you can run the Tower2csv by this simple command line call:
```
python .\main.py 
```

### Input parameters

The Tower2csv requires two inputs: 

- netcdf_dir = Directory of the netCDF files (string).

- save_file_path = Name of the .CSV file where the output data will be saved (string).

### Input data example

  Data from the OWEZ offshore meteorological tower are used to exemplify the Tower2csv applicability ([owez](Data/owez)). You can find data from other sites at the following link: 
  
  https://talltowers.bsc.es/access-the-data

#### Input database structure

  Now, let's continue by understanding the dataset structure using the data example which is uploaded here. When opening the [owez](Data/owez) folder, there is a subfolder called [10minutely](/Data/owez/10minutely):

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/4fe8815a-d4da-4547-8387-3805ad0c786d)

The data are organized in different subfolders inside [10minutely](Data/owez/10minutely), which are named according to the sensor type:

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/e25850a6-332e-4c84-a627-f4d1f5c6b835)

For instance, in the humidity-sensor folder "huragl116S1", you will see that there is one netCDF file for each month:

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/c2a5965f-2921-4de4-9e07-e15bb0f09d9a)

### Output example

One output example is in [owez.csv](Data/owez.csv). When running the [Tower2csv.py](/modules/Tower2csv.py) via [main.py](/main.py), all netCDF files from all subfolders are joined, and then, saved into a single .CSV file. Data from each sensor are stored in different comma-separated columns as follows:

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/39919ba6-3f11-41de-932d-713e3aa5dded)



