from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    buyer_name = db.Column(db.String(50), unique=True, nullable=False)
    poc_name = db.Column(db.String(50), unique=True, nullable=False)
    mobile = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gst = db.Column(db.String(60), nullable=False)

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        buyer_name = request.form.get('buyer_name')
        poc_name = request.form.get('poc_name')
        mobile = request.form.get('mobile')
        email = request.form.get('email')
        gst = request.form.get('gst')

        # Check if the username or email already exists
        existing_mobile = User.query.filter_by(mobile=mobile).first()
        existing_email = User.query.filter_by(email=email).first()

        if existing_mobile:
            flash('User already registered!', 'danger')
        elif existing_email:
            flash('User already registered!', 'danger')
        else:
            # Create a new user and add to the database
            new_user = User(buyer_name=buyer_name, poc_name=poc_name, mobile=mobile, email=email, gst=gst)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('register'))

    return render_template('register.html')

# Initialize the database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run
