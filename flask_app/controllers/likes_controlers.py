from flask import render_template, session, request, redirect, url_for
from flask_app import app
from flask_app.models.like import Like


# probably won't use this one yet..
@app.route('/api/v1/liked_rescues', methods=['GET'])
def liked_rescues():
    if 'login_id' not in session:
        return redirect(url_for('home'))

    data = {
        'user_id': session['login_id']
    }
    liked_rescues = Like.get_liked_rescues_by_user(data)
    return render_template('liked_rescues.html', liked_rescues=liked_rescues)

@app.route('/api/v1/rescues/like/<int:rescue_id>', methods=['POST'])
def user_liked_rescue(rescue_id):
    if 'login_id' not in session:
        return redirect(url_for('home'))

    data = {
        'user_id': session['login_id'],
        'rescue_id': rescue_id
    }
    Like.user_like_rescue(data)
    return redirect(url_for('dashboard'))

@app.route('/api/v1/rescues/unlike/<int:rescue_id>', methods=['POST'])
def user_unliked_rescue(rescue_id):
    if 'login_id' not in session:
        return redirect(url_for('home'))

    data = {
        'user_id': session['login_id'],
        'rescue_id': rescue_id
    }
    Like.user_unlike_rescue(data)
    return redirect(url_for('dashboard'))
