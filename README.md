The "Tower2csv.py" class scans netcdf files from a Tall-Tower database and joins all them into a single .csv file. An example of how to use it is given at the "main.py" file.

Towards this end, the Tower2csv only requires three STRING inputs: 

1 - netcdf_dir = Directory of netcdf files 

2 - year = Year of data to be joined and converted 

3 - save_dir = Directory to save the .csv file.

OUTPUT EXAMPLE

In this section we use data from the OWEZ offshore meteorological tower to exemplify what the Tower2csv does in practice. The OWEZ dataset can be downloaded at the following link: 

https://talltowers.bsc.es/access-the-data

To download the data, search for "Egmond aan zee" in the field "Tower name". Then, click on the station in the map, and after that, click on "Access to data: b2share". Then, you will download the "owez.zip" file.

Now, let's continue by understanding the dataset structure. When opening the "owez" file (or the unziped folder), there is a folder called "10minutely":

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/88a28998-6584-4e66-a616-556e6b23a530)

The data are organized in different subfolders inside "10minutely", which are named according to the sensor type:

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/3a697716-fc1e-439c-a5c3-2f0074f3b43d)

If we open, for instance, the humidity-sensor folder "huragl21S1", we will see that there is one netcdf file for each month:

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/0b73c460-3fb6-4c61-aa5f-addd5ffee83e)

The Tower2csv scans all these files, from all subfolders, and joins them into a single .csv file as follows:

![image](https://github.com/marcosp-araujo/Tower2csv/assets/88653954/6ab15a09-a489-4c81-9ca3-463b330375aa)

For doing so, the "netcdf_dir" input parameter shaw be "/owez/", i.e., the directory of the folder which holds the "10minutely" folder.

