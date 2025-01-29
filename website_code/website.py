from flask import Flask, jsonify, render_template


app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return "<h1>Home Page</h1><p>This is a simple Flask application.</p>"

# About Page
@app.route('/about')
def about():
    return "<h1>About</h1><p>This is a simple Flask application.</p>"

# API Endpoint
@app.route('/api/data')
def api_data():
    data = {"message": "Hello, this is an API response!", "status": "success"}
    return jsonify(data)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
