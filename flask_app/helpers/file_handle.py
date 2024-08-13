import os
from werkzeug.utils import secure_filename
from flask_app import app
from flask import request, flash

def allowed_files(filename):
    ALLOWED_EXTENSIONS = { 'jpeg', 'jpg', 'png' }
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_image(file):
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config('UPLOAD_FOLDER'), filename)
    print(file_path)
    file.save(file_path)
    return filename


def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        # return redirect('edit_resuce')
    
    file = request.files['file']
    if file.filename == '':
        flash('No image was selected for uploading')
        # return redirect('edit_resue')
    if file and allowed_files(file.filename):
        filename = secure_filename(file.filename)
        file.save(
            os.path.join(
                app.config('UPLOAD_FOLDER'), filename
                )
            )
        # print(f'uplaod image filename: {filename}' )
        flash('image successfully uploaded')
        # return render_template()
    else:
        flash('allowed image types are pngjpg')
        # return redirect('edit_rescue') or new_rescue