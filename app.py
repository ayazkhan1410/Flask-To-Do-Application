from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from flask import redirect, url_for
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = "super-secret-key"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/', methods=['GET', 'POST'])
def todo():
    search_query = request.form.get('search')
    
    if search_query:
        AllTodo = Todo.query.filter(Todo.title.contains(search_query)).all()
        return render_template('index.html', AllTodo=AllTodo)
    
    if request.method == "POST" and not search_query:
        title = request.form['title']
        desc = request.form['desc']
        
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

        return redirect(url_for('todo'))
        
    AllTodo = Todo.query.all()
    return render_template('index.html', AllTodo=AllTodo)

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todo'))
    
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno): 
    todo = Todo.query.filter_by(sno=sno).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()
        
    return redirect(url_for('todo'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        check_user =  User.query.filter_by(email=email).first()
        print("Login Check User: ", check_user)
        
        if check_user and check_user.check_password(password):
            session['name'] = check_user.name
            session['email'] = check_user.email
            return redirect(url_for('todo'))
        else:
            return "Invalid credentials", 400
            
    return render_template('login.html')

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        repeat_password = request.form['repeat_password']
        
        if password!= repeat_password:
            return "Passwords do not match",400
        
        print(name, email, password)
        
        check_user =  User.query.filter_by(email=email).first()
        if check_user:
            return "User already exists", 400
       
        user_obj = User(name=name, email=email, password=password)
        db.session.add(user_obj)
        db.session.commit()
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('todo'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)