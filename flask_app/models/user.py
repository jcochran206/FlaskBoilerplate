from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db_name = 'your database schema'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #cls to save to database 
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO database () Values (matching form values here %(first_name)s);'
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return result
    
    #cls to read users from database : READ
    @classmethod
    def get_all_users(cls):
        query = "select * from database table here;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    #cls to create user in db : CREATE
    @classmethod 
    def add_user(): 
        pass


    #validate form inputs
    @staticmethod 
    def validate_form():
        is_valid = True
        # need conditional statements here for each data requirement
        return is_valid