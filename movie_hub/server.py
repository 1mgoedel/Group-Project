from flask_app import app
from flask import Flask,render_template,redirect
from flask_app.models.movie import Movie 
from flask_app.controllers import users,lists,ratings,movies,comments

@app.route('/')
def go_home():
    return redirect('/splash')
@app.route('/splash')
def splash():
    top_movies = Movie.get_top_movies()
    for movie in top_movies:
        print(movie.id)
    return render_template('splash.html',top_movies=top_movies)
@app.route('/log_and_reg')
def log_and_reg():
    return render_template('log_reg.html')
@app.route('/test')
def add_movie():
    Movie.add_new_movie('My Neighbor Totoro')
    return redirect('/splash')
@app.route('/view/<int:id>')
def view_movie(id):
    data={
        'id':id
    }
    movie = Movie.get_movie_by_id(data)
    return render_template('view.html',movie=movie)

if __name__=="__main__":
    app.run(debug=True)