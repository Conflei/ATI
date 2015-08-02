from flask import *
#from models.modelo import *

app = Flask (__name__, template_folder = 'views', static_folder = 'statics')

# Routes goes here

#@app.route('/sayhello')
#def pedro():
#	name = request.args.get('name')
#	return render_template('say.html', name = name)

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

@app.route('/assets/<path:path>')
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
	#codUsuario = obtenerCodigoUsuario(name=name,password=password)
	#if codUsuario:
	#	datos = obtenerDatosUsuario(codUsuario)
#		usuario = datos['name']
#		print("usuario: "+usuario)
#	else:
#		error = 'ERROR: Correo electronico o Contrasena son invalidos.'
	#listaPasties = leerPasties(pastieP,False,codUsuario)
	#return render_template('Inicio.html',error = error, estado = estado, usuario = usuario, listaPasties = listaPasties)
	return render_template('lobby.html')

# Routes end here

if __name__ == '__main__':
  app.debug = True
  app.run( host = '0.0.0.0', port = 5000 )


