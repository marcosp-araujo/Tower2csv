## Description

The Tall Tower Dataset is an open database aimed at boosting the use of hub-height wind observations from meteorological towers. The [Tower2csv](/modules/Tower2csv) API automatically requests data to Tall Tower for a given input tower name, and then it reads and joins all netCDF into a single .CSV file, that can be downloaded.

## Web based app
Use the app through the following link:

https://tower2csv.streamlit.app/

## Running in your local machine
### Requirements and virtual environment

Creating a virtual environment is strongly advisable to avoid errors when running the Tower2csv in your local machine. It can be done using the "uv" library. You may use the following command lines in your terminal to install "uv" and set up a new virtual environment:

```
pip install uv
```
For creating a new virtual environment called "venv":
```
uv venv --python 3.12
```

Now, for activating the new virtual environment:
```
.\venv\Scripts\activate.ps1
```

Then, for installing the [requirements.txt](requirements.txt):

```
uv pip install -r requirements.txt
````

### Run web app locally
There are two options: web app and script.
The web app can be run using:
```
uv run streamlit run .\main_app.py 
```

### Run via script

If running the Tower2csv in your Python environment, you have to set the input parameters in the [main.py](.\main.py) file. For example:
```python
tower_name = 'Delvar'  # Tower name
unzip_dir = r"./Data"  # Directory to extract the netCDF files
save_file_path = f"./Data/{tower_name}" # Path to save the .csv file
```
Then, call the main.py in your terminal:
```
uv run python main.py 
```