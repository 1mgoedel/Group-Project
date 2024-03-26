from flask_app.config.mysqlconnection import connectToMySQL

class Comment:
    def __init__(self,data):
        self.user_id = data['user_id']
        self.movie_id = data['movie_id']

    @classmethod
    def add_movie_to_list(cls,data):
        query = '''INSERT INTO movies_on_list (user_id,movie_id)
                    VALUES (%(user_id)s,%(movie_id)s)'''
        results = connectToMySQL('movie_hub_schema').query_db(query,data)
        return results
