from flask_app.config.mysqlconnection import connectToMySQL

class User:
    DB = 'users_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email, created_at, updated_at ) VALUES ( %(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() );"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        # empty list to add instances of users
        users = []
        # for loop to intirate over th db results and create an instace of users with cls.
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def get_one(cls, data):
        query = " SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s; "
        return connectToMySQL(cls.DB).query_db(query, data)
