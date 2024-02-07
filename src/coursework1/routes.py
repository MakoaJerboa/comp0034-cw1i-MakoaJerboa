from flask import current_app as app

app.app_context()
@app.route('/')
def hello():
  return f"Hello!"