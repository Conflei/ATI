from flask import *

app = Flask (__name__, template_folder = 'views', static_folder = 'statics')
app = Flask (__name__)

# Routes goes here

@app.route('/')
def index():
	return 'Hello Flask'

@app.route('/sayhello')
def pedro():
	name = request.args.get('name')
	return render_template('say.html', name = name)

@app.route('/form')
def xs():
	return render_template('form.html')

@app.route('/login', methods = ['POST'])
def login():
	email = request.form['Email']
	password = request.form['Password']
	if(email == 'pedro@gmail.com'and password == '1'):
		return render_template('say.html', name = email)
	return render_template('form.html')

# Routes end here

if __name__ == '__main__':
  app.debug = True
  app.run( host = 'mesfinterest.conflei.koding.io', port = 5000 )


