# STEP 2 : CREATE AN API

from fastapi import FastAPI
import joblib
import numpy as np

# import the model:
model = joblib.load('app/model.joblib')

class_names = np.array(['setosa', 'versicolor', 'virginica'])

app = FastAPI()

# app.get method: this decorator tells test API
# that the function right below is going to handle all the coming to this path
# which is going to be the root of our web.
@app.get('/')
def reed_root():
    return {'message': 'Iris model API'}

# Sending data to the model so it would predict on that data

@app.post('/predict')
# and will create an endpoint predict with the post method and the function
# is going to receive the data which is going to be a dictionnary
# It will extract the features out of that dictionnary and make prediction to the model
# map the prediction to the classes that we have defined.
# so it will return something meaningful rather than 0 or 1 or 2 (species)
# return this response
def predict(data: dict):
    """
    Predicts the class of given set of features

    Args:
        data (dict): a dictionary containing the features to
        e.g. {"features": [1, 2, 3, 4]}
    Returns:
        dict: a dictionary containing the predicted class.
    """
    features = np.array(data['features']).reshape(1,-1)
    prediction = model.predict(features)
    class_name = class_names[prediction][0]
    return {"predicted_class": class_name}

