# Tower2csv
The "Tower2csv.py" class converts and joins netcdf-files from the Tall Tower database for a given input year into a csv file.
An example of how to use it is in the "main.py" file.

Basically, the Tower2csv requires three STRING inputs:
1 - netcdf_dir = Directory of netcdf files
2 - year = Year of data to be joined and converted
3 - save_dir = save_dir  Directory to save the .csv

WHAT THE TOWER2CSV.PY DOES?

In order to understand what the Tower2csv does, we use data from the OWEZ offshore meteorological tower as example. The dataset was dowloaded in the following link:
https://talltowers.bsc.es/access-the-data

In the link above, search for "Egmond aan zee" in the field "Tower name". Then, click on the station in the map, and after that, click on "Access to data: b2share". Then, you will download the "owez.zip" file with the data.

Let's continue by underdanding the dataset structure. When opening the "owez" folder, we a main folder called '10minutely':

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/88a28998-6584-4e66-a616-556e6b23a530)

All data are organized in different subfolders named according to the sensor type:

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/3a697716-fc1e-439c-a5c3-2f0074f3b43d)

If we open, for instance, the humidity sensor "huragl21S1", we will that there is one netcdf file for each month:

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/0b73c460-3fb6-4c61-aa5f-addd5ffee83e)

