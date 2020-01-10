import pandas as pd
import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from joblib import load
from flask import Flask, jsonify, request
import pickle

model_path = os.path.join('airbnb_src', 'model.pkl')
print(model_path)
model = load(model_path)
print('reading model')

"""Create and configure an instance of the Flask application"""
app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello World'

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'results': int(result[0])}

    # return data
    return jsonify(results=output)


if __name__ == '__main__':
    app.run()
