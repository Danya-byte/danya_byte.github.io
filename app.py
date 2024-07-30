from flask import Flask, request, jsonify, render_template
import requests
from config import OMDB_API_KEY

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    title = request.args.get('title')
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={title}"
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)