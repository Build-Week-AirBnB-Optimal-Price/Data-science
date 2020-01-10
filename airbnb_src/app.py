import pandas as pd
import os
from joblib import load
from flask import Flask, jsonify, request

model_path = os.path.join('airbnb_src', 'model.pkl')
model = load(model_path)

"""Create and configure an instance of the Flask application"""
app = Flask(__name__)

"""landing page to check if working properly"""
# @app.route('/')
# def root():
#     return 'You made it. Congrats.'

@app.route('/', methods=['GET', 'POST'])
def predict():
    # get data
    data = request.get_json(force=True)
    print(data)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    print(data_df.shape)
    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'results': int(result[0])}

    # return data
    return jsonify(results=output)


if __name__ == '__main__':
    app.run()
