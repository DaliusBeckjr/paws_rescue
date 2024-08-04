from flask_app import app 
from flask_app.controllers import users_controllers
from flask_app.controllers import rescues_controllers
from flask_app.controllers import likes_controlers







if __name__ == '__main__':
    app.run(debug = True, port = 8080)