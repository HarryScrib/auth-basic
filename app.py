from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "your_secret_key" # change this to a proper secret key in production
bcrypt = Bcrypt(app)


# configure sql alchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# database model ~ single row within our db
class User(db.Model):
    # Class variables
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)  # bcrypt produces 60-character hashes

    def set_password(self, password):
        """hash and set the user's password."""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """check if provided password matches the hash."""
        return bcrypt.check_password_hash(self.password_hash, password)
    

# routes
@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for('dashboard'))
    return render_template("index.html")


# login
@app.route("/login", methods=["POST"])
def login():
    # collect info from the form with validation
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '')
    
    # basic validation
    if not username or not password:
        return render_template("index.html", error="Please enter both username and password")
    
    user = User.query.filter_by(username=username).first()
    
    # check if it's in the db / login
    if user and user.check_password(password):
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        # provide feedback for failed login
        return render_template("index.html", error="Invalid username or password")


# register
@app.route("/register", methods=["POST"])
def register():
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '')
    
    # Basic validation
    if not username or not password:
        return render_template("index.html", error="Please enter both username and password")
    
    if len(username) < 3:
        return render_template("index.html", error="Username must be at least 3 characters long")
    
    if len(password) < 6:
        return render_template("index.html", error="Password must be at least 6 characters long")
    
    # Check if user already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return render_template("index.html", error="Username taken, please try another")
    
    try:
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        session['username'] = username
        return redirect(url_for('dashboard'))
    except Exception as e:
        db.session.rollback()
        return render_template("index.html", error="Registration failed, please try again")


# dashboard
@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return render_template("dashboard.html", username=session['username'])
    return redirect(url_for('home'))



# logout
@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


# switch to bcrypt from werkzeug

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)