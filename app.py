import flask
from flask import Flask,request
import json
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

modelfile = 'models/SVRmodel.p'
data = pickle.load(open(modelfile, 'rb'))
y_scaler = data['y_scaler']
model = data['model']


@app.route('/predict/', methods=['GET','POST'])
def predict():

	# json input
	x = request.get_json()

	# convert x to DataFrame
	col = ['age','sex','bmi','children','smoker','region']
	x = pd.DataFrame(data=[x],columns=col)

	# make prediction
	prediction = model.predict(x)
	prediction = y_scaler.inverse_transform(prediction)[0]

	response = json.dumps({'prediction':prediction})
	return response


if __name__ == '__main__': 
	app.run(debug=True)