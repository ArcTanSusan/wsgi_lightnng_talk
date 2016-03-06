from flask import Flask, request
app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
    return "Hello %s, I'm a flask app!" % (name)


# Uncomment the below in order to run this Flask app.
# if __name__ == '__main__':
#     app.debug = True
#     app.run()
