import requests
import io

def data_API(tower_name):
    ''' Data API'''
    url = f"https://b2share.eudat.eu/records/dc96d-19028/files/{tower_name}.zip?download=1"
    response = requests.get(url)
    if response.status_code == 200:
        zip_file = io.BytesIO(response.content)
    else:
        print(f"Error: received status {response.status_code} for {url}")
        return None
    
    return zip_file