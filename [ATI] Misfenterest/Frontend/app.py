from flask import *

app = Flask (__name__, template_folder = 'views', static_folder = 'static')

# Routes goes here

@app.route('/sayhello')
def pedro():
	name = request.args.get('name')
	return render_template('say.html', name = name)

@app.route('/')
def index():
	print('funciona')
	return render_template('index.html')

@app.route('/css/<path:path>')
def send_css(path):
	return send_from_directory('css', path)

@app.route('/js/<path:path>')
def send_js(path):
	return send_from_directory('js', path)

@app.route('/img/<path:path>')
def send_img(path):
	return send_from_directory('img', path)

@app.route('/<path:path>')
def send_assets(path):
	return send_from_directory('assets', path)

@app.route('/fonts/<path:path>')
def send_fonts(path):
	return send_from_directory('fonts', path)

@app.route('/form')
def xs():
	return render_template('form.html')

@app.route('/login', methods = ['POST'])
def login():
	print("Los datos que llegaron al server son "+request.form['Name']+" "+request.form['Password'])
	name = request.form['Name']
	password = request.form['Password']
	if(name == 'misaelsebin'and password == '1'):
		return render_template('say.html', name = email)
	return render_template('lobby.html')

# Routes end here

if __name__ == '__main__':
  app.debug = True
  app.run( host = '0.0.0.0', port = 5001 )


