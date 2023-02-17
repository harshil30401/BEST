import pandas as pd
import numpy as np
import random, json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, render_template, request
from python import getRecommendation

app = Flask(__name__)

df = pd.read_csv("books.csv")

def setChoices():
    genres = df.genre.unique()

    custom = df[["image", "Title", "genre", "ratingsCount"]]

    fiction = custom.loc[random.choice(custom.loc[(custom.ratingsCount > 2000) & (custom.genre == genres[0])].index)]
    # sports = custom.loc[random.choice(custom.loc[(custom.ratingsCount > 2000) & (custom.genre == genres[1])].index)]  
    music =custom.loc[random.choice(custom.loc[(custom.ratingsCount > 900) & (custom.genre == genres[2])].index)]   
    travel = custom.loc[random.choice(custom.loc[(custom.ratingsCount > 2000) & (custom.genre == genres[3])].index)]
    youndAdultFiction = custom.loc[random.choice(custom.loc[(custom.ratingsCount > 2000) & (custom.genre == genres[4])].index)]
    humour = custom.loc[random.choice(custom.loc[(custom.ratingsCount > 2000) & (custom.genre == genres[5])].index)]
    # drama = custom.loc[(custom.ratingsCount > 900) & (custom.genre == genres[6])]
    adventure = custom.loc[random.choice(custom.loc[(custom.ratingsCount > 2000) & (custom.genre == genres[7])].index)]
    # # crime = custom.loc[(custom.ratingsCount > 900) & (custom.genre == genres[8])]
    # # romances = custom.loc[(custom.ratingsCount > 2000) & (custom.genre == genres[9])]
    # # miliraty = custom.loc[(custom.ratingsCount > 2000) & (custom.genre == genres[10])]
    # horror = custom.loc[(custom.ratingsCount > 2000) & (custom.genre == genres[11])]
    topgenres = [fiction, music, travel, youndAdultFiction, humour, adventure]

    randomSamples = random.sample(topgenres, 5)

    dictionary = {}

    for i in range(5):
        dictionary[i] = randomSamples[i]
    return dictionary

# def getRecommendations(personality, favorite_books):
#     try:
#         if personality == 'Introvert':
#             genres = ['fiction', 'travel', 'drama']
#         else:
#             genres = ['sports & recreation', 'music', 'adventure stories']
#         df_filtered = df[df['genre'].isin(genres)]

#         tfidf = TfidfVectorizer(stop_words='english')
#         tfidf_matrix = tfidf.fit_transform(df_filtered['description'])

#         favorite_books_descriptions = df_filtered[df_filtered['Title'].isin(favorite_books)]['description']
#         favorite_books_tfidf = tfidf.transform(favorite_books_descriptions)
#         cosine_similarities = cosine_similarity(favorite_books_tfidf, tfidf_matrix)

#         similar_books_indices = cosine_similarities.argsort()[0][::-1]
#         similar_books = df_filtered.iloc[similar_books_indices]

#         # print(similar_books["genre"].value_counts())

#     except ValueError:
#         pass

#     # recommendations = {
#     #     "books": str(similar_books.to_dict()),
#     #     "status": "success"
#     # }
#     return similar_books.to_dict()

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
    personality = str(userPreferences["personality"])

    print(favorite_books, personality)

    # result = getRecommendation(personality, favorite_books)

    # # print(result["Title"][0], result["description"][0], result["authors"][0], result["genre"][0])
    
    return "Received"

if __name__ == "__main__":
    app.run(debug=True)