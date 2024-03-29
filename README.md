# Model for SALSA MC002 NBS Results Interpretation
The model is designed to analyze image outputs from *SALSA MC002 SMA NEWBORN SCREEN ASSAY* (MRC Holland).  
The machine used is *Applied Biosystems 7500 Real-Time PCR System*.  
The software used is *HID Real-Time PCR Analysis Software v1.2.* with default export parameters (background grid, axis and legend included).  

## What is included?
This repository includes:
1) .h5 file (saved model with both structure and weights)
2) static folder with .html page
3) .py flask backend
4) examples of input images
5) .ipynb file used for model training

## What should I install in order to run this model?
The prerequisites are following:
1) Python 3.X
2) Tensorflow and it's dependencies
3) Flask library

## How can I run it locally?  
```  
pip3 install tensorflow python3-flask  
git clone https://github.com/trickovicmatija/SMA.git  
cd SMA
export FLASK_APP=predict_app.py
flask run --host=127.0.0.1  
```  
In order to run the model, you should:
1) Install the prerequisites
2) Clone the repository on local machine via "git clone"
3) Run the flask script
4) Manually navigate to "/static/index.html" in address bar
5) Upload the image and predict the outcome



**This is created as a part of Master's thesis at the Centre for Human Molecular Genetics, University of Belgrade - Faculty of Biology.**
