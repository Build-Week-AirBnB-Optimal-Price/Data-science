from flask import Flask, render_template, request
import numpy as np

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def sentiment_analysis(input):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(input)
    rating = scores.get('compound')
    return rating


def create_app():
    app = Flask(__name__)

    @app.route('/', methods = ['GET', 'POST'])
    def root():
        return render_template('base.html')

    @app.route('/analyze', methods = ['GET', 'POST'])
    def analysis(message = ''):

        text = request.values['description_text']
        prediction = sentiment_analysis(text)
        description = text
        message = f"On a scale of -1 to 1, your description's positivity is {prediction}."

        return render_template('prediction.html', description = description, message = message)

    return app
