INTRODUCTION

  The "Tower2csv.py" class scans netcdf files from a Tall-Tower database and joins all netCDF files from a given year into a single .csv file. An example of how to use it is provided in the "main.py" file.

INPUTS

Towards this end, the Tower2csv only requires three inputs: 

1 - netcdf_dir = Directory of netcdf files (string).

2 - year = Year of data to be joined and converted (number).

3 - save_dir = Directory to save the .csv file (string).

DATA EXAMPLE

  Data from the OWEZ offshore meteorological tower to are used exemplify the Tower2csv applicability. You can find some OWEZ-database example files in the "owez" folder within this repository. The whole OWEZ database can be downloaded at the following link: 

  https://talltowers.bsc.es/access-the-data
  
  To download the data, search for "Egmond aan zee" in the field "Tower name". Then, click on the station in the map, and after that, click on "Access to data: b2share". Then, you will download the "owez.zip" file.

NETCDF DATA STRUCTURE

  Now, let's continue by understanding the dataset structure using the data example that is here. When opening the "owez" folder, there is subfolder called "10minutely":

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/4fe8815a-d4da-4547-8387-3805ad0c786d)

The data are organized in different subfolders inside "10minutely", which are named according to the sensor type:

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/e25850a6-332e-4c84-a627-f4d1f5c6b835)

If we open, for instance, the humidity-sensor folder "huragl116S1", we will see that there is one netcdf file for each month:

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/c2a5965f-2921-4de4-9e07-e15bb0f09d9a)

OUTPUT EXAMPLE

When running the Tower2csv.py via the main.py, the first scans all these files, from all subfolders, and joins the data into a single .csv file. Data from each sensor are separately stored in different columns as follows:

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/39919ba6-3f11-41de-932d-713e3aa5dded)



