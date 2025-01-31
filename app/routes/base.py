from flask import Blueprint, render_template, Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

from app.routes.user import User

base_route = Blueprint('base_route', __name__)


@base_route.route('/')
@login_required
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'], userrole = session['userrole'])
    else:
        return redirect(url_for('login'))
    
@base_route.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        print(f"{username} {password}")
        if username == "toto" and password== "titi":
            session['username'] = username
            session['userrole'] = 'user' 
            #session['userrole'] = 'technician'
            #session['userrole'] = 'admin'
            user = User(username)
            login_user(user)
            return redirect(url_for('base_route.home'))
        else:
            return render_template('login.html', error="Identifiants incorrects.")
    
    return render_template('login.html', error=None)

@base_route.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    logout_user()
    return redirect(url_for('base_route.login'))