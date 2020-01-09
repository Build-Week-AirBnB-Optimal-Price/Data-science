import pandas as pd
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
import pickle

# create df
trainval = pd.read_csv('final3_airbnb.csv') # change file path

# drop null values
trainval.dropna(inplace=True)

# features and target
target = 'price'
features = ['host_since','zipcode','room_type','maximum_nights','minimum_nights','extra_people','accommodates','neighbourhood',
'beds','property_type','cancellation_policy','guests_included','bedrooms','bathrooms']

# X matrix, y vector
def wrangle(X):
    X = X.copy()
    return X

train_rentals, val_rentals = train_test_split(trainval, random_state=42)
train = wrangle(train_rentals)
val = wrangle(val_rentals)
target = 'price'
X_train = train.drop(columns=target)
X_val = val.drop(columns=target)
y_train = train[target]
y_val = val[target]

# X = train[features]
# y = train[target]

# model
model = make_pipeline(
    ce.OrdinalEncoder(),
    RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
)

model.fit(X_train, y_train)
model.predict(X_val)
# model.score(X, y)

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