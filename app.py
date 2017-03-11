from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin


application = Flask(__name__)
#TODO: remove cors before deployment...use for development of UI
CORS(application)

@application.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return application.send_static_file(path)


#Kick off the server
if __name__ == '__main__':
    application.run(debug=True)

