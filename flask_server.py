#!/usr/bin/python3.7
#region --Import Packages--

'''
SETUP:
 - Navigate to project directory on terminal, ensure that depeendancies are installed
 - Install needed pip3 and pip packages: try running the scripts to see which ones are needed
 - export FLASK_APP=server.py
 - python3 -m flask run (or just flask run, if your default is python3)
'''
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


#region --Initialize App, MySQL, AWS --
app = Flask(__name__)
'''
#ReactJS Route
app = Flask(__name__, static_folder='./build')

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("./build/" + path):
        return send_from_directory('./build', path)
    else:
        return send_from_directory('./build', 'index.html')


if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)'''

#Begin Helper Routes
@app.route('/myRoute', methods=['POST'])
def identifyImage():
    print("Hello World")
#endregion
