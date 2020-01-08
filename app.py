from decouple import config
import pandas as pd
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sklearn.linear_model import LogisticRegression
import pickle

# create df
train = pd.read_csv('final3_airbnb.csv') # change file path
# drop null values
train.dropna(inplace=True)
# features and target
target = 'price'
features = ['host_since','zipcode','room_type','maximum_nights','minimum_nights','extra_people','accommodates','neighbourhood',
'beds','property_type','cancellation_policy','guests_included','bedrooms','bathrooms']
# X matrix, y vector
X = train[features]
y = train[target]
# model
model = RandomForestRegressor()
model.fit(X, y)
model.score(X, y)

pickle.dump(model, open('model.pkl', 'wb'))
model = pickle.load(open('model.pkl', 'rb'))

DB = SQLAlchemy()

"""Create and configure an instance of the Flask application"""
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

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
