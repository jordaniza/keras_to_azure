# keras_to_azure
Codebase for deploying keras model to azure container

This repo contains the files and folders necessary to run a Docker instance in an Azure Container.

# Docker
The relevant Docker Registry is jzia93/predixa-keras-model:working-version-1

The Dockerfile is included in the repo. Note: due to compatability issues with Tensorflow 2.1.X we force Tensorflow 2.0.0. This is for the following reasons:

- Models trained in Google Colab require TF 2.X or greater
- TF versions > 2.0.0 appear to have compatability issues when loading Keras models

There are also issues with Python 3.8, Tensorflow and Docker. For this reason we force Python 3.6 in the Dockerfile.

# app.py

Contains the logic for the app. As of current version the app has 2 functions:

app.route('/') Returns status if passed a blank GET request
app.route('/get-category-prediction') takes a serialised numpy array in JSON format and generates a prediction from the Keras model on file. 

The numpy array should have shape (None, None, Number_of_categories) as the CNN is a Fully Convolutional Network and can take variable input shapes.

# model.hdf5

Model trained using tensorflow.keras Sequential CNN. The Model is a Fully Convolutional Network trained on Google Colab.

the app and example python files reference the model using a relative path. If saving the model to a separate directory as the python files make sure to amend the directory.


# example_payload.py

Used for testing Flask and Docker implementations locally. Uses the request library to send POST requests of randomised data to whatever URL.

Note, when testing Docker, make sure Flask bindings are set to '0.0.0.0' and that the localhost IP is at 127.0.0.1

# requirements.txt

Docker dependencies file, current build:

- python 3.6 
- tensorflow 2.0.0
- numpy
- json
- flask

# Azure

The model is *currently* hosted in an Azure Container Instance (ACI) at predixa-dynamix.eastus.azurecontainer.io

# areas for improvement:

- Troubleshoot timeout issue with ACI
- Add validations on input size and shape - we have none at the moment
- Add proper error handling & messaging in app.py - we have none at the moment
- The Keras model in this repo needs to be replaced with a properly trained one, same format but this one is a throwaway
- Need to migrate the Docker registry to private
- Forgot to remove debug mode from flask
