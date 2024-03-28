from flask_app.config.mysqlconnection import connectToMySQL

class List:
    def __init__(self,data):
        self.id=data['id']
        self.user_id=data['user_id']
        self.name = data['name']

    @classmethod
    def get_users_lists(cls,data):
        query = '''SELECT * FROM lists
                    WHERE user_id = %(id)s'''
        results = connectToMySQL('movie_hub_schema').query_db(query,data)
        lists=[]
        for list in results:
            lists.append(cls(list))
        return lists
    @classmethod
    def add_list(cls,data):
        query = '''INSERT INTO lists (user_id,name)
                    VALUES (%(user_id)s,%(name)s)'''
        results = connectToMySQL('movie_hub_schema').query_db(query,data)
        return results
    @classmethod
    def get_list_by_id(cls,data):
        query = '''SELECT * FROM lists
                    WHERE id = %(id)s'''
        results = connectToMySQL('movie_hub_schema').query_db(query,data)
        return results[0]