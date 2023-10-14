from flask import Flask
import logging
from flask.logging import create_logger


app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route('/')
def home():
	<h2 style='text-align: center;'> The greatest team to EVER: The Arsenal Invincibles </h2>"
	<p> The invincibles had a record of 24 wins and 12 draws and 0 loses. </br> 
	No one has come close to this record, many have attempted but none have succeeded. undefined</br>
	The spine of the team was formed by the likes of Patrick Vieira, Thierry Henry, Robert Pires, Sol Campbell, Dennis Bergkamp, and Ashley Cole. </br>
	These players, along with others such as Gilberto Silva, Lauren, Freddie Ljungberg, and Jens Lehmann, formed a formidable unit that possessed both flair and work rate.
	</p>"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True) #port=80
