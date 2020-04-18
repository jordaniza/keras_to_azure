from numpy import expand_dims, random
import json
import requests
from tensorflow.keras.models import load_model

number_of_statements = random.randint(50, 100)
number_of_respondents = random.randint(10, 30)
number_of_categories = 18

sample_request = random.randn(number_of_statements, number_of_respondents, number_of_categories)
# sample_request = expand_dims(sample_request, axis=0)
# sample_request = np.transpose(sample_request, (0, 1, 2, 3))

print(sample_request.shape)

data = {"arr":sample_request.tolist()}

"""
model = load_model('model-50-0.503.hdf5')
print(model.predict(sample_request))
"""

#url = "http://localhost:5000/get-category-prediction"
url = "http://127.0.0.1:8888/get-category-prediction"
headers = {'Content-Type': 'application/json'}

response = requests.request("POST", url, headers=headers, json = data).json()

print(f'Predictions: {response}')

