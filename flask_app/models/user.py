from flask_app.config.mysqlconnetcion import connectToMySQL



class User:
    db = "users_rescues_schema"
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# create
    @classmethod 
    def create_user(cls, data):
        query = """ 
            INSERT INTO users
            (first_name, last_name, email, password)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod 
    def get_user_by_email(cls, data):
        query = ''' 
            SELECT * FROM users
            WHERE email = %(email)s;
        '''
        results = connectToMySQL(cls.db).query_db(query, data)

        if len(results) < 1:
            return False

        return cls(results[0])

# get user by id
    @classmethod 
    def get_user_by_id(cls, data):
        query = ''' 
            SELECT * FROM users
            WHERE id = %(id)s;
        '''
        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

