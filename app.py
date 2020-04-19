from flask import Flask, request
import json
from numpy import expand_dims, array 
from tensorflow.keras.models import load_model

app = Flask(__name__)

# check the app is alive

@app.route('/')
def is_alive():
    return f'Yes, the app is alive.'

# main application, gets data from POST request
# the body of the request will be a json object created from a numpy array

@app.route('/get-category-prediction', methods = ['POST'])
def generate_prediction():
    if request.method == 'POST':

        data = request.get_json()

        # transform the data from the serialised JSON into a numpy array
        # note, we do the transformations here, but could do it on the application side
        
        data = data['arr']


        # remember that numpy has been preloaded
        
        data = array(data)
        data = expand_dims(data, axis=0)

        # keras model has been loaded
        # note we assume statements, respondents, categories

        model = load_model('model-50-0.503.hdf5')
        output = model.predict(data)
    
        output = json.dumps(output.tolist())

        return output
    
# includes localhost bindings for docker debugging in local

if __name__ == '__main__':
    app.run(host = '0.0.0.0')

