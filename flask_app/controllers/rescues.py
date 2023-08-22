from flask_app.models import user, rescue
from flask import render_template, session, request, redirect
from flask_app import app

@app.route('/rescues/dashboard')
def dashboard():
    if 'login_id' not in session:
        return redirect('/')
    data = {
        'id' : session['login_id']
    }
    return render_template('dashboard.html', all_rescues = rescue.Rescue.get_all_rescues(), one_user = user.User.get_user_by_id(data))


@app.route('/rescues/new')
def new_rescue():
    if 'login_id' not in session:
        return redirect('/')

    return render_template('new_rescue.html')


@app.route('/rescues/create', methods = ['POST'])
def create_rescue():
    if 'login_id' not in session:
        return redirect('/')

    val_rescue = rescue.Rescue.validate_rescue(request.form)

    if not val_rescue:
        return redirect('/rescues/new')

    rescue.Rescue.save_rescue(request.form)
    return redirect ('/rescues/dashboard')


@app.route('/rescues/edit/<int:id>')
def edit_rescues(id):
    if 'login_id' not in session:
        return redirect('/')

    data = {
        'id': id
    }
    return render_template('edit_rescue.html', one_rescue = rescue.Rescue.get_one_rescue(data))


@app.route('/rescues/update', methods = ['POST'])
def update_rescues():
    if 'login_id' not in session:
        return redirect('/')
    val_rescue = rescue.Rescue.validate_rescue(request.form)

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