import os
import zipfile

# Install Kaggle
os.system("pip install kaggle")

# Download dataset from Kaggle
os.system("kaggle datasets download -d sammd4/spd-5k -p dataset/")

# Extract the zip file
zip_path = "dataset/spd-5k.zip"

if os.path.exists(zip_path):
    print("Extracting dataset...")
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall("dataset/")
    print("Extraction complete.")
else:
    print("Dataset ZIP file not found!")