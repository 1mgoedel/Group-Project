from flask_app.config.mysqlconnection import connectToMySQL

class Rating:
    def __init__(self,data):
        self.user_id = data['user_id']
        self.movie_id = data['movie_id']
        self.rating = data['rating']

    @classmethod
    def add_rating(cls,data):
        query = '''INSERT INTO ratings (user_id,movie_id,rating)
                    VALUES (%(user_id)s,%(movie_id)s,%(rating)s)'''
        results = connectToMySQL('movie_hub_schema').query_db(query,data)
        return results