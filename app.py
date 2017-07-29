#flask modules
from flask import Flask,  jsonify, make_response, abort, request, render_template,redirect,url_for
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/')
def main():

	return render_template('index.html')

@app.route('/experience')
def experience():
	# print "in experience"
	# print url_for('experience')

	return render_template('experience.html')

@app.route('/about')
def about():
	# print "in about"
	# print url_for('about')

	return render_template('about.html')

@app.route('/contact')
def contact():
	# print "in contact"


	return render_template('contact.html')

@app.route('/portfolio')
def portfolio():
	# print "in portfolio"
	# print url_for('about')

	return render_template('portfolio.html')


#always goes at the bottom of the page

#app doesn't cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

##has to do with the WSGI
if __name__ == '__main__':
    app.run(debug=True)