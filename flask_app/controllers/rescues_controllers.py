from flask_app.models.user import User
from flask_app.models.rescue import Rescue
from flask_app.models.like import Like
from flask_app.helpers.file_handle import allowed_files, save_image
from flask import render_template, session, request, redirect, url_for
from flask_app import app
from werkzeug.utils import secure_filename
import os

@app.route('/api/v1/rescues/dashboard')
def dashboard():
    if 'login_id' not in session:
        return redirect(url_for('home'))
    data = {
        'id': session['login_id']
    }
    
    all_rescues = Rescue.get_all_rescues()

    for rescue in all_rescues:
        rescue.liked= Like.check_if_liked({
            'user_id': session['login_id'],
            'rescue_id': rescue.id
        })


    return render_template('dashboard.html', all_rescues=all_rescues, one_user=User.get_user_by_id(data))



@app.route('/api/v1/rescues/new', methods = ['GET'])
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

    # Validate form data and files
    new_rescue = Rescue.validate_rescue(data, files)
    if not new_rescue:
        return redirect(url_for('new_rescue'))

    # Handle file upload
    file = files.get('file')
    image_path = None
    if file and allowed_files(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        image_path = os.path.join('images', 'uploads', filename)

    # Prepare data for database
    rescue_data = {
        'name': data['name'],
        'description': data['description'],
        'breed': data['breed'],
        'location': data['location'],
        'age': data['age'],
        'gender': data['gender'],
        'size': data['size'],
        'fixed': data['fixed'],
        'type': data['type'],
        'image_path': image_path,
        'user_id': session['login_id']
    }

    # Insert data into the database
    result = Rescue.create_rescue(rescue_data)
    if result:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('new_rescue'))



@app.route('/api/v1/rescues/edit/<int:id>', methods = ['GET'])
def edit_rescues(id):
    if 'login_id' not in session:
        return redirect(url_for('home'))

    data = {
        'id' : id
    }

    return render_template('edit_rescue.html', one_rescue = Rescue.get_one_rescue(data))

@app.route('/api/v1/rescues/update', methods=['POST'])
def update_rescues():
    if 'login_id' not in session:
        return redirect(url_for('home'))

    data = request.form
    files = request.files

    # Check if 'id' is in the form data
    rescue_id = data.get('id')
    if not rescue_id:
        return redirect(url_for('dashboard'))

    # Validate form data and files
    valid_rescue = Rescue.validate_rescue(data, files)
    if not valid_rescue:
        return redirect(url_for('edit_rescues', id=rescue_id))

    # Handle file upload
    file = files.get('file')
    image_path = data.get('existing_image_path')  # Preserve existing image path if no new file

    if file and allowed_files(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        image_path = os.path.join('images', 'uploads', filename)

    # Prepare data for database update
    rescue_data = {
        'id': rescue_id,
        'name': data['name'],
        'description': data['description'],
        'breed': data['breed'],
        'location': data['location'],
        'age': data['age'],
        'gender': data['gender'],
        'size': data['size'],
        'fixed': data['fixed'],
        'type': data['type'],
        'image_path': image_path,
        'user_id': session['login_id']
    }

    # Update the rescue record
    Rescue.update_rescue(rescue_data)
    return redirect(url_for('show_rescue', id=rescue_id))


@app.route('/api/v1/rescues/show/<int:id>')
def show_rescue(id):
    if 'login_id' not in session:
        return redirect(url_for('home'))
    data = {
        'id': id
    }
    rescue = Rescue.get_one_rescue(data)
    if rescue:
        return render_template('view_rescue.html', one_rescue=rescue)
    else:
        return redirect(url_for('dashboard'))

@app.route('/api/rescues/delete', methods=['POST'])
def delete_rescue():
    Rescue.delete_rescue(request.form)
    return redirect(url_for('dashboard'))
