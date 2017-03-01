from flask import Flask


# Create instance of the Flask class
app = Flask(__name__)

@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True)
