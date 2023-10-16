from flask import Flask, render_template, request, redirect, url_for, flash
from user_manager import UserManager

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a strong secret key

user_manager = UserManager(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if user_manager.authenticate_user(username, password):
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login failed. Check your credentials.', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if user_manager.register_user(username, password):
            flash('Registration successful!', 'success')
            return redirect(url_for('success'))  # Redirect to the success page
        else:
            flash('Registration failed. Username may be taken.', 'danger')
    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
