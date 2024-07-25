from flask import flash
def validate_rescue(data):
    is_valid = True
    
    
    if len(data['name']) == 0:
        is_valid = False
        flash('Name can not be left empty', 'rescue')
    elif len(data['name']) < 3:
        is_valid = False
        flash('Name must be at least 3 characters or more', 'rescue')
    if len(data['description']) > 200:
        is_valid = False
        flash('Description can not be left empty', 'rescue')
    if len(data['breed']) == 0:
        is_valid = False
        flash('breed can not be empty', 'rescue')
    if len(data['age']) == 0:
        is_valid = False
        flash('Age can not be empty', 'rescue')
    # gener
    if 'gender' not in data:
        is_valid = False
        flash('Gender option must be selected', 'rescue')
    return is_valid
    # image
    if 'image' not in data:
        is_valid = False
        flash('')
    # size
    if 'size' not in data:
        is_valid = False
        flash('size option must be selected', 'rescue')
    return is_valid
    # fixed
    if 'fixed' not in data:
        is_valid = False
        flash('Fixed option must be selected', 'rescue')
    return is_valid
