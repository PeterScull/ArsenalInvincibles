from flask import Flask
import logging
from flask.logging import create_logger


app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route('/')
def home():
 return "<h1 style='text-align: center;'>We Are The Invincibles</h1>"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True) #port=80
