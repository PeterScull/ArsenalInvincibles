from flask import Flask
import logging
from flask.logging import create_logger


app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route('/')
def home():
	header = "<h2 style='text-align: center;'> The greatest team to EVER: The Arsenal Invincibles </h2>"
	paragraph = "<p> The invincibles had a record of 24 wins and 12 draws and 0 loses. No one has come close to this record, many have attempted but none have succeeded. </p>"
	return header + paragraph
	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True) #port=80
