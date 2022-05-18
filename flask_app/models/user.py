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
        query = 'INSERT INTO database name here'
        result = connectToMySQL(db_name).query_db(query,data)
        return result
    
    #cls to read users from database
    @classmethod
    def get_all_users():
        query = "select * from database table here"
        results = connectToMySQL(db_name).query_db(query);
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    #