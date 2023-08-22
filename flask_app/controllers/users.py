from flask_app import app, bcrypt
from flask import render_template, redirect, session, request
from flask_app.models import user, rescue


@app.route('/')
def home():
    return render_template('login_reg.html')

# made to keep the user password a secret in mysql database 
# when user is registering for a new acc
@app.route('/users/register', methods = ['POST'])
def register():
    if not user.User.validate_register(request.form):
        return redirect('/')
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : hashed_pw
    }
    one_user_id = user.User.save(data)
    session['login_id'] = one_user_id
    return redirect('/rescues/dashboard')


@app.route('/users/login', methods = ['POST'])
def login():
    one_user = user.User.validate_login(request.form)

# if user already exist he is sent back to register
    if not one_user:
        return redirect('/')

# if he does not exist passes them through to the bands dashboard
    session['login_id'] = one_user.id
    return redirect('/rescues/dashboard')

# made to log out the user and take them back to the register page
@app.route('/users/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/users/rescues/<int:id>')
def my_rescue(id):
    data = {
        'id' : id
    }
    user_data = {
        'id' : id
    }
    one_user = user.User.get_user_by_id(user_data)
    return render_template('my_rescues.html', all_rescue = rescue.Rescue.get_one_rescue(data), one_user = one_user)

