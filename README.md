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
### python download_coco.py
### python download_style_images.py
### python data_preprocessing.py
### python train.py
### streamlit run app.py

