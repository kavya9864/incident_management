from flask import Flask, request, jsonify, session, redirect, url_for, render_template
import sqlite3

from flask import Flask
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incidents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create tables if they don't exist
with app.app_context():
    db.create_all()

# Initialize Flask app
app = Flask(__name__)

# Secret key to secure session data
app.secret_key = 'your_secret_key_here'

# Database connection function (adjust to your needs)
def get_db_connection():
    conn = sqlite3.connect('your_database.db')  # Change to your actual DB
    conn.row_factory = sqlite3.Row
    return conn

# Home route
@app.route('/')
def index():
    # Check role from session
    if 'role' in session:
        role = session['role']
    else:
        role = None
    return render_template('index.html', role=role)  # Pass role to template

# Login route (dummy login, set role in session)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form['role']
        session['role'] = role  # Store role in session
        return redirect(url_for('index'))  # Redirect to home page
    return '''
        <form method="post">
            <label>Select Role:</label>
            <select name="role">
                <option value="admin">Admin</option>
                <option value="user">User</option>
            </select>
            <input type="submit" value="Login">
        </form>
    '''

# Route to resolve incidents (only admin can resolve)
@app.route('/incident/<int:id>/resolve', methods=['PATCH'])
def resolve_incident(id):
    if session.get('role') != 'admin':  # Check if the user is admin
        return jsonify({'error': 'Unauthorized'}), 403  # Unauthorized if not admin
    conn = get_db_connection()
    conn.execute('UPDATE incidents SET status = ? WHERE id = ?', ('Resolved', id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Incident marked as resolved'})

# Route to view incidents (can be viewed by any logged-in user)
@app.route('/incidents', methods=['GET'])
def view_incidents():
    conn = get_db_connection()
    incidents = conn.execute('SELECT * FROM incidents').fetchall()
    conn.close()
    return render_template('incidents.html', incidents=incidents)

# Route to create a new incident (admin only)
@app.route('/incident/create', methods=['GET', 'POST'])
def create_incident():
    if session.get('role') != 'admin':  # Only admin can create incidents
        return jsonify({'error': 'Unauthorized'}), 403  # Unauthorized if not admin

    if request.method == 'POST':
        incident_name = request.form['incident_name']
        incident_description = request.form['incident_description']

        conn = get_db_connection()
        conn.execute(
            'INSERT INTO incidents (name, description, status) VALUES (?, ?, ?)',
            (incident_name, incident_description, 'Open')
        )
        conn.commit()
        conn.close()

        return redirect(url_for('view_incidents'))  # Redirect to incident list after creation

    return '''
        <h2>Create New Incident</h2>
        <form method="post">
            <label for="incident_name">Incident Name:</label><br>
            <input type="text" id="incident_name" name="incident_name" required><br><br>
            <label for="incident_description">Incident Description:</label><br>
            <textarea id="incident_description" name="incident_description" required></textarea><br><br>
            <input type="submit" value="Create Incident">
        </form>
        <br>
        <a href="/">Back to Home</a>
    '''

# Route to log out (clear session)
@app.route('/logout', methods=['GET'])
def logout():
    session.clear()  # Clear session data
    return redirect(url_for('index'))  # Redirect to home page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

