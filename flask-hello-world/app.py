# ---- Flask Hello World ---- #

# imports the flask package
from flask import Flask

# creates app object
app = Flask(__name__)

# use the decorator pattern to
# link the view function to a url
@app.route("/")
@app.route("/hello")

# defines the view with a function, and returns a string
def hello_world():
	return "Hello, World!"

#starts the dev server using the  run() method
if __name__ == "__main__":
	app.run()
