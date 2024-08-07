from flask_app import app, bcrypt
from flask import render_template, redirect, session, request, url_for
from flask_app.models.user import User
from flask_app.models.rescue import Rescue

@app.route('/')
def home():
    return render_template('login_reg.html')

# made to keep the user password a secret in mysql database 
# when user is registering for a new acc
@app.route('/users/register', methods = ['POST'])
def register():
    
    check_reg = User.validate_register(request.form)

    if not check_reg:
        return redirect(url_for('home'))

#   using bcrypt to hash the newly register users password
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : hashed_pw
    }
#   this is calling the function from the user model to save user information in the db
    one_user_id = User.create_user(data)

#   now we are grabbing all the data and logging in the user but also putting the user in session
    session['login_id'] = one_user_id
    return redirect(url_for('dashboard'))


@app.route('/users/login', methods = ['POST'])
def login():
    one_user = validate_login(request.form)

# if user already exist he is sent back to register
    if not one_user:
        return redirect(url_for('home'))

# if he does not exist passes them through to the bands dashboard
    session['login_id'] = one_user.id
    return redirect(url_for('dashboard'))

# made to log out the user and take them back to the register page
@app.route('/users/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/api/users/rescues/<int:id>')
def my_rescue(id):
    data = {
        'id' : id
    }
    user_data = {
        'id' : id
    }
    one_user = User.get_user_by_id(user_data)
    return render_template('my_rescues.html', all_rescue = Rescue.get_one_rescue(data), one_user = one_user)

