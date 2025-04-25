from flask import Flask, render_template, request, redirect, url_for

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

if __name__ == '__main__':
    app.run(debug=True, port=8070) 