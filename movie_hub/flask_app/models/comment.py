from flask_app.config.mysqlconnection import connectToMySQL

class Comment:
    def __init__(self,data):
        self.user_id = data['user_id']
        self.movie_id = data['movie_id']
        self.comment = data['comment']

    @classmethod
    def add_comment(cls,data):
        query = '''INSERT INTO comments (user_id,movie_id,comment)
                    VALUES (%(user_id)s,%(movie_id)s,%(comment)s)'''
        results = connectToMySQL('movie_hub_schema').query_db(query,data)
        return results