from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('search', '')
    return f"Search results for: {query}"

if __name__ == '__main__':
    app.run(debug=True, port=8070) 