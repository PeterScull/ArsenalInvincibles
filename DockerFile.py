FROM flask import flask

app =Flask(name)

@app.route('/')
def home():
	return "<h2 style='text-aligned: center:'> The greatest team to EVER </h2>"
	return "<h1> style='text-aligned: center:'> The Arsenal Invincibles </h1>"
	Return "<p> The invicibles had a record of 24 wins and 12 draws and 0 LOSES. Noone has come close to this record, many have attempted but no have succeeded. </p>"

if _name_=="_main_":
	app.run(host='0.0.0.0', port=80, debug=True) #port=80
