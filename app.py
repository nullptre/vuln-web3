from flask import Flask, render_template, request, redirect, url_for
import requests
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import subprocess
from flask_talisman import Talisman

# Feature flag for CSP
ENABLE_CSP = True

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure CSP
csp = {
    'default-src': "'self'",
    'script-src': "'self'",  # Blocks inline scripts
    'style-src': "'self'",
    'img-src': "'self'",
    'object-src': "'none'",
    'base-uri': "'self'",
    'form-action': "'self'",
    'frame-ancestors': "'none'",
    'block-all-mixed-content': ""  # Empty string instead of True
}

# Initialize Talisman with CSP only if feature flag is enabled
if ENABLE_CSP:
    talisman = Talisman(
        app,
        content_security_policy=csp,
        content_security_policy_nonce_in=['script-src'],
        force_https=False  # For local development
    )

# In-memory storage for comments
comments = []

# Initialize database and create some test users
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    # Add some test users
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'admin123')")
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('user1', 'password1')")
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('user2', 'password2')")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('search', '')
    return f"Search results for: {query}"

@app.route('/comments')
def show_comments():
    return render_template('comments.html', comments=comments)

@app.route('/comment', methods=['POST'])
def add_comment():
    comment = request.form.get('comment', '')
    if comment:
        comments.append(comment)
    return redirect(url_for('show_comments'))

@app.route('/fetch')
def fetch_url():
    url = request.args.get('url', '')
    if url:
        try:
            response = requests.get(url)
            return f"Content from {url}:<br><pre>{response.text}</pre>"
        except Exception as e:
            return f"Error fetching URL: {str(e)}"
    return "Please provide a URL parameter"

@app.route('/users')
def search_users():
    username = request.args.get('username', '')
    if username:
        # Vulnerable SQL query - susceptible to SQL injection
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}'"
        c.execute(query)
        users = c.fetchall()
        conn.close()
        return render_template('users.html', users=users, query=query)
    return render_template('users.html', users=[], query='')

@app.route('/ping')
def ping_host():
    host = request.args.get('host', '')
    if host:
        try:
            # Vulnerable command execution - susceptible to command injection
            command = f"ping -c 4 {host}"
            result = subprocess.check_output(command, shell=True, text=True)
            return render_template('ping.html', result=result)
        except subprocess.CalledProcessError as e:
            return render_template('ping.html', result=f"Error: {str(e)}")
    return render_template('ping.html')

if __name__ == '__main__':
    init_db()  # Initialize database on startup
    app.run(debug=True, port=8070) 