from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.movie import Movie

class Movies_on_list:
    def __init__(self,data):
        self.user_id = data['user_id']
        self.movie_id = data['movie_id']
        self.is_watched = data['is_watched']
        self.list_id = data['list_id']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.movies = []

    @classmethod
    def add_movie_to_list(cls,data):
        query = '''INSERT INTO movies_on_list (list_id,movie_id,user_id,is_watched,created_at,updated_at)
                    VALUES (%(list_id)s,%(movie_id)s,%(user_id)s,0,now(),now())'''
        results = connectToMySQL('movie_hub_schema').query_db(query,data)
        return results
    
    @classmethod
    def get_movies_on_list(cls,data):
        query = '''SELECT * FROM movies_on_list
                    LEFT JOIN users on users.id = user_id
                    LEFT JOIN movies on movies.id = movie_id
                    WHERE list_id = %(id)s'''
        results = connectToMySQL('movie_hub_schema').query_db(query,data)
        movies_on_list = []
        for row in results:
            movie_data = {
                'id': row['movie_id'],
                'title': row['title'],
                'poster': row['poster'],
                'plot': row['plot'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            movie = Movie(movie_data)
            movies_on_list.append(movie)
        return movies_on_list
    @classmethod
    def delete_movie_from_list(cls,data):
        query = '''DELETE FROM movies_on_list 
                    WHERE movie_id = %(movie_id)s AND list_id = %(list_id)s'''
        results = connectToMySQL('movie_hub_schema').query_db(query,data)
        return results

    

        
    
        
