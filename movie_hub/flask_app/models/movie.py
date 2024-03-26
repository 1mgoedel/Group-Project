from flask_app.config.mysqlconnection import connectToMySQL
import requests
import os
import urllib.parse
from flask import flash

class Movie:
    def __init__(self,data):
        self.title = data['title']
        self.poster = data['poster']
        self.desc = data['desc']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_movies(cls):
        query = '''SELECT * FROM movies'''
        result = connectToMySQL('movie_hub_schema').query_db(query)
        movies = []
        for movie in result:
            movies.append(cls(movie))
        return movies
    @classmethod
    def add_new_movie(cls,user_movie_name):
        movie_name = urllib.parse.quote(user_movie_name)
        response = requests.get(f'http://www.omdbapi.com/?i=tt3896198&apikey=90c66df5&t={movie_name}')
        if response.status_code == 200:
            movie_data = response.json()
            movie_title = movie_data['Title']
            movie_desc = movie_data['Plot']
            image_url = movie_data['Poster']
            movie_poster = cls.save_poster_locally(movie_title,image_url)
            sql_data={
                'title':movie_title,
                'poster':movie_poster,
                'desc':movie_desc
            }
            cls.save_movie_to_db(sql_data)
        else:
            flash('no movie data found','movie')
            print(f"API request failed with status code: {response.status_code}")
            return response
        print('Movie added successfully')
        return response
        
    @classmethod
    def save_movie_to_db(cls,data):
        query = '''INSERT INTO movies (title,poster,desc,created_at,updated_at)
                    VALUES (%(title)s,%(poster)s,%(desc)s,now(),now())'''
        result = connectToMySQL('movie_hub_schema').query_db(query,data)
        return result

    @staticmethod
    def save_poster_locally(movie_name,image_url):
        movie_name_formatted = movie_name.replace(' ','_')
        image_filename = f'{movie_name_formatted}.jpg'
        image_path = os.path.join('/movie_poster',image_filename)
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(f'flask_app/static/'+image_path,'wb') as image_file:
                image_file.write(response.content)
            print('image written to file')
            return image_path
        else:
            print(f"Failed to download image from {image_url}. Status code: {response.status_code}")
            return None


        