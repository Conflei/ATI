from flask import *
import modelo
import psycopg2

app = Flask (__name__, template_folder = 'views', static_folder = 'statics')

pageP = 1;



#####################################################################################################################
#modeloo################################################

def existUser (name,password):

	#print("obtenerCodUsuarioooo")

	dbConnection = psycopg2.connect('dbname=atidatabase user=postgres password=123 host=localhost')
	cursor = dbConnection.cursor()

	cursor.execute('select name from users where name=%s and password=%s',(name,password))

	if cursor.rowcount == 0:
		return False

	cursor.close()
	dbConnection.close()

	return True

def  obtenerDatosUsuario (name):
	dbConnection = psycopg2.connect('dbname=atidatabase user=postgres password=123 host=localhost')
	cursor = dbConnection.cursor()

	datos = {}
	cursor.execute('select fullname from users where name=%s',(name))

	tmp = cursor.fetchone()
	datos['fullname'] = tmp[0]

	cursor.close()
	dbConnection.close()

	return datos

def searchPin(pageP,name):
	dbConnection = psycopg2.connect('dbname=atidatabase user=postgres password=123 host=localhost')
	cursor = dbConnection.cursor()

	listPin = []
	cursor.execute('select picdir from pictures offset %s limit 5',((pageP-1)*7))
	
	dataPin = cursor.fetchall();

	for dPin in dataPin:
		Pin = {}
		Pin['url'] = dPin[0]
		listPin.append(Pin)

	cursor.close()
	dbConnection.close()

	return listPin





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
	exist = existUser(name=name,password=password)
	error = ""
	if exist:
		datos = obtenerDatosUsuario(name)
		usuario = datos['fullname']
		print("usuario: "+usuario)
	else:
		error = 'ERROR: Correo electronico o Contrasena son invalidos.'
	listPin = searchPin(pageP,name)
	return render_template('lobby.html',error = error, usuario = usuario, listPin = listPin)

# Routes end here

if __name__ == '__main__':
  app.debug = True
  app.run( host = '0.0.0.0', port = 5000 )

