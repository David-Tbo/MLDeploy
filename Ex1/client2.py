# STEP 5: automate inference (more than one observation)

# The real intention for model deployment is to use it programmatically.
# Some data are collected in a database and you need to send some data to the model to predict.

# This is where API

# Let's create a simple inference script called client.py
# and we use this to send the data from to an API and receive the response.

import json
import requests

data = [[5.1, 3.5, 1.4, 0.3],
        [5.7, 3.8, 1.7, 0.3]]

# Endpoint location
url = 'http://0.0.0.0:8000/predict/'

predictions = []

for record in data:
    payload = {'features': record} # Create the dictionary
    payload = json.dumps(payload) # Convert the data into json format and send them to this url
    # using the requests library, and store the reply in the response variable
    response = requests.post(url, data=payload)
    predictions.append(response)

# print the predictions
print(predictions)
