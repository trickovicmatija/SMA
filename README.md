# Model for Medical Data Analysis
This repository contains commented Jupyter Notebook file, where the model was created.
The model is designed to analyze image outputs from *SALSA MC002 SMA NEWBORN SCREEN ASSAY* (MRC Holland).
The machine used is *Applied Biosystems 7500 Real-Time PCR System*.
The software used is *HID Real-Time PCR Analysis Software v1.2.*

**Includes:**
1) .h5 file (saved model with both structure and weights)
2) static folder with .html page
3) .py flask backend
4) an example of an input
5) .ipynb file used for model training

**Prerequisites:**
1) Python 3.X
2) Tensorflow and it's dependencies
3) Flask

**In order to run locally:**
1) Install the prerequisites
2) Clone the repository on local machine via "git clone"
3) Run the flask script with "FLASK_APP=predict_app.py flask run" in terminal
4) Manually navigate to "/static/index.html"
5) Upload the image and predict the outcome

**This is created as a part of Master's thesis at the Centre for Human Molecular Genetics, University of Belgrade - Faculty of Biology.**
