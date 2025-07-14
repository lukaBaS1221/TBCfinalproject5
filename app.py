from flask_login import LoginManager
from ext import app
from models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

import routes


if __name__ == '__main__':
    app.run(debug=True)
