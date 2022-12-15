import spacy
nlp = spacy.load('en_core_web_md')

## define class
class Movie(object):
    def __init__(self,lable,description):
          self.label = lable
          self.description = description

## define function called movies
def load_movies ():
    movies = []
    with open ("movies.txt","r+") as f:
        for line in f:
            movie_line = line
            movie_line = movie_line.split(" :")
            movie = movie_line[0]
            movie_description = movie_line[1]
            movie_object = Movie(movie, movie_description)
            movies.append(movie_object)
    return movies      

## define function to recommend movie
def movie_to_recommend (description):  
    similarity_correlation = 0 
    the_movie_to_recommend = None   
    nlp_description = nlp(description)
    for movie in movies:
        similarity = nlp(movie.description).similarity(nlp_description)  
        if similarity > similarity_correlation:
            the_movie_to_recommend = movie
            similarity_correlation = similarity
    return the_movie_to_recommend


## Main Program
movies = load_movies()
description = '''
    Will he save their world or destory it? When the Hulk becoms too dangerous for the Earth, 
    the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.
    Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''
recommendation = movie_to_recommend(description)
print(recommendation.label)
print(recommendation.description)