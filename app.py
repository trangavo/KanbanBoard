from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db = SQLAlchemy(app)

# define the database
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    to_do = db.Column(db.Boolean)
    doing = db.Column(db.Boolean)
    done = db.Column(db.Boolean)

# define a route to get the data
@app.route('/')
def index():
    to_do = Task.query.filter_by(to_do=True).all()
    doing = Task.query.filter_by(doing=True).all()
    done = Task.query.filter_by(done=True).all()
    return render_template('index.html', to_do = to_do, doing = doing, done = done)

# define a route to add new data to database
@app.route('/add', methods=['POST'])
def add():
    newtask = Task(text=request.form['newitem'], to_do = True, doing = False, done = False)
    try:
        db.session.add(newtask)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return 'There was an issue adding the task.'

# define routes to update the attributes of each data instance

@app.route('/move_to_doing/<id>')
def move_to_doing(id):
    task = Task.query.filter_by(id=int(id)).first()
    try:
        task.doing = True
        task.to_do = False
        task.done = False
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return 'There was an issue updating the task.'

@app.route('/move_to_done/<id>')
def move_to_done(id):
    task = Task.query.filter_by(id=int(id)).first()
    try:
        task.doing = False
        task.done = True
        task.to_do = False
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return 'There was an issue updating the task.'

@app.route('/move_to_todo/<id>')
def move_to_todo(id):
    task = Task.query.filter_by(id=int(id)).first()
    try:
        task.doing = False
        task.done = False
        task.to_do = True
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return 'There was an issue updating the task.'
@app.route('/delete/<id>')
def delete(id):
    task = Task.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return 'There was an issue deleting the task.'

if __name__ == '__main__':
    app.run(debug=True)
