from flask import Flask, render_template, request, jsonify
import pickle
import requests
import json
import numpy as np

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# def sentiment_analysis(input):
#     sid = SentimentIntensityAnalyzer()
#     scores = sid.polarity_scores(input)
#     rating = scores.get('compound')
#     return rating

sid = SentimentIntensityAnalyzer()

pickle.dump(sid, open('model.pkl', 'wb'))

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

# @app.route('/')
# def root():
#     return render_template('base.html', methods = ['POST'])

@app.route('/', methods = ['GET', 'POST'])
def analysis():

    text = request.get_json(force = True)
    prediction = model.polarity_scores(str(text))
    # output = prediction.get('compund')

    return jsonify(results = prediction)

if __name__ == '__main__':
    app.run()
