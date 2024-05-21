from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/create_user", methods=['POST'])
def create_user():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    User.create_user(data)
    return redirect('/all_users')

@app.route('/all_users')
def all_users():
    #call the get all classmethod to get all users
    users = User.get_all_users()
    return render_template('users.html', users = users)

@app.route('/edit/user/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    return render_template('/edit.html', user = User.get_one(data))

@app.route('/user/update', methods=['POST'])
def update():
    data = {
        "id": request.form['user_id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    User.update(data)
    return redirect(f'/user/{data["id"]}')

@app.route('/user/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/all_users')

@app.route('/user/<int:id>')
def one_user(id):
    data = {
        "id": id
    }
    return render_template('view.html', user = User.get_one(data))