from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///votes.db'
db = SQLAlchemy(app)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stance = db.Column(db.String(50), nullable=False)
    votes = db.Column(db.Integer, default=0)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_stance = request.form['stance']
        vote = Vote.query.filter_by(stance=selected_stance).first()
        vote.votes += 1
        db.session.commit()
    stances = Vote.query.all()
    return render_template('index.html', stances=stances)

if __name__ == '__main__':
    db.create_all()
    app.run()
