from flask_app.models.user import User
from flask_app.models.rescue import Rescue
from flask import render_template, session, request, redirect, url_for
from flask_app import app
from werkzeug.utils import secure_filename
import os

@app.route('/rescues/dashboard')
def dashboard():
    if 'login_id' not in session:
        return redirect(url_for('home'))
    data = {
        'id' : session['login_id']
    }
    return render_template('dashboard.html', all_rescues = Rescue.get_all_rescues(), one_user = User.get_user_by_id(data), title= 'Paws Rescues | dashboard')


@app.route('/rescues/new')
def new_rescue():
    if 'login_id' not in session:
        return redirect(url_for('home'))

    return render_template('new_rescue.html')



@app.route('/rescues/create', methods=['POST'])
def create_rescue():
    if 'login_id' not in session:
        return redirect(url_for('home'))
#   retrieve uploaded file from the form
    file = request.files['image']
#   Ensures the file name is secure and removes any unsafe letters
    filename = secure_filename(file.filename)
#   created the filepath by joining the uploaded folder path with the secure file name
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#   Save the file to the specified file path on the server.
    file.save(filepath)

    if not Rescue.validate_rescue(request.form):
        return redirect('/rescues/new')

    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'breed': request.form['breed'],
        'address': request.form['address'],
        'age': request.form['age'],
        'gender': request.form['gender'],
        'size': request.form['size'],
        'fixed': request.form['fixed'],
        'type': request.form['type'],
        'image_path': filepath,
        'user_id': session['login_id'] # Assuming user_id is stored in session
    }

    Rescue.create_rescue(data)
    return redirect('/rescues/dashboard')


@app.route('/rescues/edit/<int:id>')
def edit_rescues(id):
    if 'login_id' not in session:
        return redirect('/')

    data = {
        'id': id
    }
    return render_template('edit_rescue.html', one_rescue = Rescue.get_one_rescue(data))


@app.route('/rescues/update', methods = ['POST'])
def update_rescues():
    if 'login_id' not in session:
        return redirect('/')
    val_rescue = Rescue.validate_rescue(request.form)

    if not val_rescue:
        return redirect(f"/rescues/edit/{request.form['id']}")

    rescue.Rescue.update_rescue(request.form)
    return redirect(f'/rescues/show/{request.form["id"]}')
    # return redirect('/rescues/dashboard')


@app.route('/rescues/show/<int:id>')
def show_rescue(id):
    if 'login_id' not in session:
        return redirect('/')
    data = {
        'id' : id
    }

    return render_template('view_rescue.html', one_rescue = rescue.Rescue.get_one_rescue(data))


@app.route('/rescues/delete', methods = ['POST'])
def delete_rescue():
    rescue.Rescue.delete_rescue(request.form)
    return redirect('/rescues/dashboard')