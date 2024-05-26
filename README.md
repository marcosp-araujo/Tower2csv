INTRODUCTION
  The Tall Tower is an open database aimed at boosting the use of hub-height wind observations from meteorological towers.
  The "Tower2csv.py" class scans netCDF files from a Tall Tower database and joins all of them into a single .CSV file. A "how to" example is provided in the "main.py" file.

INPUTS

The Tower2csv requires three inputs: 

1 - netcdf_dir = Directory of the netCDF files (string).

2 - save_dir = Directory to save the .CSV (string).

3 - save_file = Name of the .CSV file to be saved (string).

DATA EXAMPLE

  Data from the OWEZ offshore meteorological tower are used to exemplify the Tower2csv applicability. You can find data from other sites at the following link: 

  https://talltowers.bsc.es/access-the-data

netCDF DATABASE STRUCTURE

  Now, let's continue by understanding the dataset structure using the data example which is uploaded here. When opening the "owez" folder, there is a subfolder called "10minutely":

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/4fe8815a-d4da-4547-8387-3805ad0c786d)

The data are organized in different subfolders inside "10minutely", which are named according to the sensor type:

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/e25850a6-332e-4c84-a627-f4d1f5c6b835)

For instance, in the humidity-sensor folder "huragl116S1", you will see that there is one netCDF file for each month:

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/c2a5965f-2921-4de4-9e07-e15bb0f09d9a)

OUTPUT EXAMPLE

When running the "Tower2csv.py" via "main.py", all netCDF files from all subfolders are joined, and then, saved into a single .CSV file. Data from each sensor are stored in different comma-separated columns as follows:

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/39919ba6-3f11-41de-932d-713e3aa5dded)



