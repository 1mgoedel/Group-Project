from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.movie import Movie
from flask_app.models.rating import Rating

@app.route('/movies')
def list_movies():
    movies = Movie.get_all()
    return render_template('movies/splash.html', movies=movies)

@app.route('/movies/<int:movie_id>')
def movie_details(movie_id):
    movie = Movie.get(movie_id)
    return render_template('movies/profiles.html', movie=movie)