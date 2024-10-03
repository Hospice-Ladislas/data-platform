import requests
from datetime import datetime
from google.cloud import storage
import json

gs_client = storage.Client()
# project_id = "data-platform-436510"
# dataset_id = "Raw_Data"
# table_id = "Countries"
# table_ref = f"{project_id}.{dataset_id}.{table_id}"


def collect_data():
    """Collect data from API URL"""
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")
        return []


def upload_to_gcs(destination_gs_bucket_name, destination_gs_blob_name, src_filename):
    """Load file into GCS."""
    bucket = gs_client.get_bucket(destination_gs_bucket_name)
    blob = bucket.blob(f"{destination_gs_blob_name}/{src_filename}")
    blob.upload_from_filename(src_filename)
    print("End of uploading file")


# Sauvegarde temporaire des données dans un fichier JSON local
countries_data = collect_data()

filename = "countries_data_"+datetime.now().strftime("%Y%m%d")+".json"

with open(filename, 'w') as f:
    for country in countries_data:
        json.dump(country, f)
        f.write('\n')

upload_to_gcs("data-raw-files", "Countries", filename)

