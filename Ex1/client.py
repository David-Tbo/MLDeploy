# STEP 5: automate inference (one observation)

# The real intention for model deployment is to use it programmatically.
# Some data are collected in a database and you need to send some data to the model to predict.

# This is where API

# Let's create a simple inference script called client.py
# and we use this to send the data from to an API and receive the response.

import json
import requests

data = {'features': [1,2,3,4]}

# Endpoint location
url = 'http://0.0.0.0:8000/predict/'

# Convert the data into json format and send them to this url
data = json.dumps(data)

# using the requests library, and store the reply in the response variable
response = requests.post(url, data)

# print the response
print(response.json())
