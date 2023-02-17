import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('dataset.csv')

personality = 'Introvert'
favorite_books = ['The Lost Continent']

def getRecommendation(personality, favorite_books):
    try:
        if personality == 'Introvert':
            genres = ['fiction', 'travel', 'drama']
        else:
            genres = ['sports & recreation', 'music', 'adventure stories']
        df_filtered = df[df['genre'].isin(genres)]

        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(df_filtered['description'])

        favorite_books_descriptions = df_filtered[df_filtered['Title'].isin(favorite_books)]['description']
        favorite_books_tfidf = tfidf.transform(favorite_books_descriptions)
        cosine_similarities = cosine_similarity(favorite_books_tfidf, tfidf_matrix)

        similar_books_indices = cosine_similarities.argsort()[0][::-1]
        similar_books = df_filtered.iloc[similar_books_indices]

    except ValueError:
        pass

    return similar_books.to_dict()

res = getRecommendation(personality, favorite_books)

print(df.genre.unique())
