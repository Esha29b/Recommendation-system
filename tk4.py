import pandas as pd

movies = pd.DataFrame({
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['Salaar', 'Bad Newz', 'Leo', 'Dhamaal', 'Jailer'],
    'genre': ['Action', 'Romantic', 'Action', 'Comedy', 'Action'],
    'director': ['Prashanth Neel', 'Anand Tiwari', 'Lokesh Kanagaraj', 'Indra Kumar', 'Nelson Dilipkumar'],
    'main_actors': ['Prabhas, Shruti Haasan', 'Tripti, Vicky', 'Vijay, Trisha Krishnan', 'Sanjay, Arshad', 'Rajinikanth, Tamannaah ']
})
user_profile = {
    'genre': 'Action',
    'director': 'Nelson Dilipkumar',
    'main_actors': 'Rajinikanth, Tamannaah'
}
def compute_similarity(movie, user_profile):
    score = 0
    if movie['genre'] == user_profile['genre']:
        score += 1
    if movie['director'] == user_profile['director']:
        score += 1
    if any(actor in movie['main_actors'] for actor in user_profile['main_actors'].split(', ')):
        score += 1
    return score

movies['similarity'] = movies.apply(lambda row: compute_similarity(row, user_profile), axis=1)
recommended_movies = movies.sort_values(by='similarity', ascending=False)

print(recommended_movies[['title', 'similarity']])