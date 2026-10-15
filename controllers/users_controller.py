from flask import render_template,request,redirect,url_for,session,flash
from flask_bcrypt import Bcrypt
#importar el modelo de user

def init_user_routes(app):

    @app.route('/')
    def index():
        if 'user_id' in session:
            return redirect(url_for('dashboard'))

        return render_template(index.html)