from flask_app.models.user import User
from flask_app.models.rescue import Rescue
from flask import render_template, session, request, redirect, url_for
from flask_app import app
from werkzeug.utils import secure_filename
import os

@app.route('/api/v1/rescues/dashboard')
def dashboard():
    if 'login_id' not in session:
        return redirect(url_for('home'))
    data = {
        'id' : session['login_id']
    }
    return render_template('dashboard.html', all_rescues = Rescue.get_all_rescues(), one_user = User.get_user_by_id(data))


@app.route('/api/v1/rescues/new')
def new_rescue():
    if 'login_id' not in session:
        return redirect(url_for('home'))

    return render_template('new_rescue.html')



@app.route('/api/v1/rescues/create', methods=['POST'])
def create_rescue():
    if 'login_id' not in session:
        return redirect(url_for('home'))
    
    data = request.form
    files = request.files

    new_rescue = Rescue.validate_rescue(data, files)
    if not new_rescue:
        return redirect(url_for('new_rescue'))

    # file handling..
    file = files.get('image_path')
    if file and file.filename:
        filename = secure_filename('file.filename')
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        image_path = filepath



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
        'image_path': image_path,
        'user_id': session['login_id'] # Assuming user_id is stored in session
    }

    Rescue.create_rescue(data)
    return redirect(url_for('dashbord'))


@app.route('/api/v1/rescues/edit/<int:id>')
def edit_rescues(id):
    if 'login_id' not in session:
        return redirect(url_for('home'))

    data = {
        'id': id
    }
    return render_template('edit_rescue.html', one_rescue = Rescue.get_one_rescue(data))


@app.route('/api/v1/rescues/update', methods = ['POST'])
def update_rescues():
    if 'login_id' not in session:
        return redirect(url_for('home'))
    val_rescue = Rescue.validate_rescue(request.form)

    if not val_rescue:
        return redirect(f"/api/v1/rescues/edit/{request.form['id']}")

    Rescue.update_rescue(request.form)
    return redirect(f'/api/v1/rescues/show/{request.form["id"]}')
    # return redirect('/rescues/dashboard')


@app.route('/api/v1/rescues/show/<int:id>')
def show_rescue(id):
    if 'login_id' not in session:
        return redirect(url_for('home'))
    data = {
        'id' : id
    }

    return render_template('view_rescue.html', one_rescue = Rescue.get_one_rescue(data))


@app.route('/api/rescues/delete', methods = ['POST'])
def delete_rescue():
    Rescue.delete_rescue(request.form)
    return redirect('/rescues/dashboard')