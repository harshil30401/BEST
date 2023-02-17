import pandas as pd
import numpy as np
import random, json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, render_template, request
# from python import getRecommendation

app = Flask(__name__)

df = pd.read_csv("dataset.csv")

def setChoices():
    genres = df.genre.unique()

    custom = df[["image", "Title", "genre", "ratingsCount"]]

    fiction = custom.loc[random.choice(custom.loc[(custom.ratingsCount > 2000) & (custom.genre == genres[0])].index)]
    music =custom.loc[random.choice(custom.loc[(custom.ratingsCount > 900) & (custom.genre == genres[2])].index)]   
    travel = custom.loc[random.choice(custom.loc[(custom.ratingsCount > 2000) & (custom.genre == genres[3])].index)]
    youndAdultFiction = custom.loc[random.choice(custom.loc[(custom.ratingsCount > 2000) & (custom.genre == genres[4])].index)]
    humour = custom.loc[random.choice(custom.loc[(custom.ratingsCount > 2000) & (custom.genre == genres[5])].index)]
    adventure = custom.loc[random.choice(custom.loc[(custom.ratingsCount > 2000) & (custom.genre == genres[7])].index)]
    topgenres = [fiction, music, travel, youndAdultFiction, humour, adventure]

    randomSamples = random.sample(topgenres, 5)

    dictionary = {}

    for i in range(5):
        dictionary[i] = randomSamples[i]
    return dictionary

def getRecommendation(personality, user_favorites):
    if personality == 'introvert':
        df = df[df['introvert'] == 1]
    else:
        df = df[df['extrovert'] == 1]

    vectorizer = CountVectorizer()
    title_vectors = vectorizer.fit_transform(df['Title'])

    user_vectors = vectorizer.transform(user_favorites)

    similarity_scores = cosine_similarity(user_vectors, title_vectors)

    recommendations_indices = similarity_scores.argsort()[0][::-1]
    recommendations = df.iloc[recommendations_indices]
    return recommendations

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get5books', methods=["GET"])
def set_choices():

    dictionary = setChoices()
    choices = {

        0 : {
            "image" : dictionary[0]["image"],
            "Title" : dictionary[0]["Title"],
            "genre" : dictionary[0]["genre"]
        },
        1 : {
            "image" : dictionary[1]["image"],
            "Title" : dictionary[1]["Title"],
            "genre" : dictionary[1]["genre"]
        },
        2 : {
            "image" : dictionary[2]["image"],
            "Title" : dictionary[2]["Title"],
            "genre" : dictionary[2]["genre"]
        },
        3 : {
            "image" : dictionary[3]["image"],
            "Title" : dictionary[3]["Title"],
            "genre" : dictionary[3]["genre"]
        },
        4 : {
            "image" : dictionary[4]["image"],
            "Title" : dictionary[4]["Title"],
            "genre" : dictionary[4]["genre"]
        },
    }

    return choices


@app.route('/recommendation', methods=["POST"])
def getPreferences():

    userPreferences = request.get_json()
    
    favorite_books = list(userPreferences["books"])
    personality = str(userPreferences["personality"]).lower()

    print(favorite_books, personality)

    if personality == 'introvert':
        d = df[df['introvert'] == 1]
    else:
        d = df[df['extrovert'] == 1]

    vectorizer = CountVectorizer()
    title_vectors = vectorizer.fit_transform(d['Title'])

    user_vectors = vectorizer.transform(favorite_books)

    similarity_scores = cosine_similarity(user_vectors, title_vectors)

    recommendations_indices = similarity_scores.argsort()[0][::-1]
    recommendations = d.iloc[recommendations_indices]

    context = (recommendations.to_dict(orient='records'))

    print(context)
    return context
    # return render_template('recommendation.html', **context)

if __name__ == "__main__":
    app.run(debug=True)
