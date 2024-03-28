from flask_app import app
from flask import Flask,render_template,redirect,request,session
from flask_app.models.movie import Movie 
from flask_app.models.movies_on_list import Movies_on_list
from flask_app.models.list import List
from flask_app.models.user import User
from flask_app.controllers import users,lists,ratings,movies,comments

@app.route('/')
def go_home():
    return redirect('/splash')
@app.route('/splash')
def splash():
    top_movies = Movie.get_top_movies()
    return render_template('splash.html',top_movies=top_movies)
@app.route('/log_and_reg')
def log_and_reg():
    return render_template('log_reg.html')
@app.route('/add_movie',methods=['POST'])
def add_movie():
    Movie.add_new_movie(request.form['title'])
    list_id = request.form['list_id']
    return redirect(f'/new_list/{list_id}')
@app.route('/view/<int:id>')
def view_movie(id):
    data={
        'id':id
    }
    movie = Movie.get_movie_by_id(data)
    return render_template('view.html',movie=movie)
@app.route('/dashboard')
def dashboard():
    user_id = session['user_id']
    data = {
        'id':user_id
    }
    user = User.get_user_by_id(data)
    lists = List.get_users_lists(data)
    return render_template('dashboard.html',lists=lists,user=user)
@app.route('/new_list/<int:list_id>')
def new_list(list_id):
    
    all_movies = Movie.get_all_movies()
    user_data ={
        'id':session['user_id']
    }
    user = User.get_user_by_id(user_data)
    data={
        'id':list_id
    }
    list_data = {
        'id':list_id
    }
    movies_on_list = Movies_on_list.get_movies_on_list(data)
    for movie in movies_on_list:
        print(movie.id)
    list = List.get_list_by_id(list_data)
    return render_template('new_list.html',all_movies=all_movies,movies_on_list=movies_on_list,list=list,user=user)
@app.route('/new_list/add',methods=['POST'])
def add_list():
    list_user = request.form['user_id']
    list_name = request.form['list_name']
    data = {
        'user_id':list_user,
        'name':list_name
    }
    list_id = List.add_list(data)
    return redirect(f'/new_list/{list_id}')
@app.route('/new_list/add_movie',methods=['POST'])
def add_movie_to_list():
    movie_id=request.form['movie_id']
    user_id=request.form['user_id']
    list_id=request.form['list_id']
    data = {
        'user_id':user_id,
        'movie_id':movie_id,
        'list_id':list_id
    }
    Movies_on_list.add_movie_to_list(data)
    return redirect(f'/new_list/{list_id}')
@app.route('/new_list/delete_movie',methods=['POST'])
def delete_movie_from_list():
    list_id = request.form['list_id']
    data = {
        'movie_id':request.form['movie_id'],
        'list_id':list_id
    }
    Movies_on_list.delete_movie_from_list(data)
    return redirect(f'/new_list/{list_id}')

if __name__=="__main__":
    app.run(debug=True)