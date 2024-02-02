'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)
'''

from flask import current_app as app

app.app_context()
@app.route('/')
def hello():
  return f"Hello!"

'''
if __name__ == "__main__":
    app.run(debug=True)
'''