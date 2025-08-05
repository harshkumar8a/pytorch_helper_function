import requests
import zipfile
from pathlib import Path

def getDatasetsUsingLink(
  image_path_data, 
  url
):
  # Setup path to data folder
  data_path = Path("data/")
  image_path = data_path / "{image_path_data}"
  
  # If the image folder doesn't exist, download it and prepare it... 
  if image_path.is_dir():
      print(f"{image_path} directory exists.")
  else:
      print(f"Did not find {image_path} directory, creating one...")
      image_path.mkdir(parents=True, exist_ok=True)
      
      # Download data
      with open(data_path / "{image_path_data}.zip", "wb") as f:
          request = requests.get("{url}")
          print("Downloading datasets....")
          f.write(request.content)
  
      # Unzip data
      with zipfile.ZipFile(data_path / "{image_path_data}.zip", "r") as zip_ref:
          print("Unzipping datasets...") 
          zip_ref.extractall(image_path)
