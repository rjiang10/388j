from flask_app import create_app 

def handler(event, context):
  return create_app.wsgi_app(event, context)