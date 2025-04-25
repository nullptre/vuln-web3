from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)
comments = []  # In-memory storage for comments

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

if __name__ == '__main__':
    app.run(debug=True, port=8070) 