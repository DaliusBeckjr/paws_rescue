from flask import flash
from flask_app.models.user import User
from flask_bcrypt import bcrypt

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