import requests
import io

def data_API(site):
    ''' Data API'''
    site = site.lower()
    url = f"https://b2share.eudat.eu/api/files/8f2778c4-b1c1-4fc5-90b6-c17b34154efc/{site}.zip"
    response = requests.get(url)
    if response.status_code == 200:
        zip_file = io.BytesIO(response.content)

    return zip_file