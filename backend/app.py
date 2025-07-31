import flask, flask_cors

app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.route('/')
def test():
    return 'Hello World!'

@app.route('/recommendations/<title>')
def recommendations(title):
    pass

if __name__ == '__main__':
    app.run(debug=True, port=5000)