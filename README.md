# Create a Virtual Environment:
## On Windows:
### python -m venv venv
### venv\Scripts\activate

## On macOS/Linux:
### python3 -m venv venv
### source venv/bin/activate


# Install Dependencies:
pip install -r requirements.txt

# order of running the python scripts:
### cd src
### python download_coco.py (change the number of images you want to download)
### python download_style_images.py (change the number of images you want to download)
### python data_preprocessing.py
### python train.py
### streamlit run app.py

