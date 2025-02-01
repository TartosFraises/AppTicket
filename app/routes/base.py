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
        password = request.form['password_hash']
        if username == "admin" and password== "MfemXjFVhqwZi9eYtmKc5JA9CJlHbVdBqfMuLlIbamY=": # admin/toto
            session['username'] = username
            session['userrole'] = 'admin'
            user = User(username)
            login_user(user)
            return redirect(url_for('base_route.home'))
        elif username == "user" and password== "MfemXjFVhqwZi9eYtmKc5JA9CJlHbVdBqfMuLlIbamY=": # user/toto
            session['username'] = username
            session['userrole'] = 'user' 
            user = User(username)
            login_user(user)
            return redirect(url_for('base_route.home'))
        elif username == "tech" and password== "MfemXjFVhqwZi9eYtmKc5JA9CJlHbVdBqfMuLlIbamY=": # tech/toto
            session['username'] = username
            session['userrole'] = 'technician'
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
    
@base_route.route('/about')
@login_required
def about():
    if 'username' in session:
        return render_template('about.html', username=session['username'], userrole = session['userrole'])
    else:
        return redirect(url_for('login'))

@base_route.route('/tickets')
@login_required
def tickets():
    if 'username' in session:
        return render_template('tickets.html', username=session['username'], userrole = session['userrole'])
    else:
        return redirect(url_for('login'))
        
@base_route.route('/update_user')
@login_required
def update_user():
    if 'username' in session:
        return render_template('update_user.html', username=session['username'], userrole = session['userrole'])
    else:
        return redirect(url_for('login'))
        
        
@base_route.route('/all_tickets')
@login_required
def all_tickets():
    if 'username' in session:
        return render_template('all_tickets.html', username=session['username'], userrole = session['userrole'])
    else:
        return redirect(url_for('login'))
        
@base_route.route('/config_users')
@login_required
def config_users():
    if 'username' in session:
        return render_template('config_users.html', username=session['username'], userrole = session['userrole'])
    else:
        return redirect(url_for('login'))



@base_route.route('/assigned_tickets')
@login_required
def assigned_tickets():
    if 'username' in session:
        return render_template('assigned_tickets.html', username=session['username'], userrole = session['userrole'])
    else:
        return redirect(url_for('login'))


@base_route.route('/statistics')
@login_required
def statistics():
    if 'username' in session:
        return render_template('statistics.html', username=session['username'], userrole = session['userrole'])
    else:
        return redirect(url_for('login'))