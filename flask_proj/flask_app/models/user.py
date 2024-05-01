from flask_app.config.mysqlconnetcion import connectToMySQL
from flask_app.models import rescue
from flask_app import app, bcrypt
from flask import flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



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
        self.rescues = []

# create
    @classmethod 
    def save(cls, data):
        query = """ 
            INSERT INTO users
            (first_name, last_name, email, password)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL(cls.db).query_db(query, data)

# crud method: read
    # @classmethod
    # def get_all_users(cls, data):
    #     query = """ 
    #         SELECT * FROM users
    #         JOIN rescues ON rescues.user_id = users.id
    #         WHERE users.id = %(id)s;
    #     """
    #     results = connectToMySQL(cls.db).query_db(query, data)
        
    #     one_user = cls( results[0] )
        
    #     for row in results:
    #         rescue_data = {
    #             'id' : row['rescue.id'],
    #             'name' : row['name'],
    #             'description' : row['description'],
    #             'breed' : row['breed'],
    #             'location' : row['location'],
    #             'age' : row['age'],
    #             'gender' : row['gender'],
    #             'size' : row['size'],
    #             'fixed' : row['fixed'],
    #             'type' : row['type'],
    #             'created_at' : row['rescue.created_at'],
    #             'updated_at' : row['rescue.updated_at'],
    #             'user_id' : row['user_id'],
    #         }
    #         one_user.rescues.append( rescue.Rescue(rescue_data) )
    #         return one_user


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

# update

# delete

# validation
    @staticmethod 
    def validate_register(data):
        is_valid = True
        one_user = User.get_user_by_email(data)

# if user already exist in the database
        if one_user:
            is_valid = False
            flash('login in, please', 'reg')


# validate_first_name ->
        if len(data['first_name']) == 0:
            is_valid = False
            flash('First Name can not be left empty', 'reg')
# validate_last_name    ->
        if len(data['last_name']) == 0:
            is_valid = False
            flash('Last Name can not be left empty', 'reg')
# validate_email    ->
        if len(data['email']) == 0:
            is_valid = False
            flash('Email can not be left empty', 'reg')
        elif not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('Invalid email format', 'reg')
# validate_password    ->
        if len(data['password']) == 0:
            is_valid = False
            flash('Password can not be left empty', 'reg')
# validate_confirm_pw ->
        if len(data['confirm_pw']) == 0:
            is_valid = False
            flash('Confirm Password can not be left empty', 'reg')
# match: password
        if data['password'] != data['confirm_pw']:
            is_valid = False
            flash('Passwords do not match')
        return is_valid

    @staticmethod 
    def validate_login(data):
        is_valid = True

        one_user = User.get_user_by_email(data)

# if user already exist in the database
        if not one_user:
            flash('Invalid Credentials', 'login')
            return False

        if not bcrypt.check_password_hash(one_user.password, data['password']):
            flash('Invalid Credentials', 'login')
            return False
        return one_user