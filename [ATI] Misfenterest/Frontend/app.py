from flask import *
import modelo
import psycopg2

app = Flask (__name__, template_folder = 'views', static_folder = 'statics')

pageP = 1;



#####################################################################################################################
#modeloo################################################

def existUser (name,password):

	print("obtenerCodUsuarioooo")

	dbConnection = psycopg2.connect('dbname=atidatabase user=postgres password=123 host=localhost')
	cursor = dbConnection.cursor()

	cursor.execute('select name from users where name=%s and password=%s',(name,password))
	print("executed")
	if cursor.rowcount == 0:
		cursor.close()
		dbConnection.close()
		print("not founded")
		return False

	cursor.close()
	dbConnection.close()
	print("founded")
	return True

def  obtenerDatosUsuario (name):

	dbConnection = psycopg2.connect('dbname=atidatabase user=postgres password=123 host=localhost')
	cursor = dbConnection.cursor()

	datos = {}
	print("ENTREEEEEE "+name)
	cursor.execute('select * from users where name=%s',[name]) 
	print("ENTREEEEEE 33")
	tmp = cursor.fetchone()
	datos['fullname'] = tmp[0]

	cursor.close()
	dbConnection.close()

	return datos

def searchPin(pageP,name):
	dbConnection = psycopg2.connect('dbname=atidatabase user=postgres password=123 host=localhost')
	cursor = dbConnection.cursor()

	listPin = []
	cursor.execute('select picdir from pictures offset %s limit 5',[((pageP-1)*7)])
	
	dataPin = cursor.fetchall();

	for dPin in dataPin:
		Pin = {}
		Pin['url'] = dPin[0]
		listPin.append(Pin)

	cursor.close()
	dbConnection.close()

	return listPin

def crearCuenta (newName, newPassword, newEmail, newFullname):
	dbConnection = psycopg2.connect('dbname=atidatabase user=postgres password=123 host=localhost')
	cursor = dbConnection.cursor()

	if(not existUser(newName, newPassword)):
		cursor.execute('insert into users (name, passord, email, fullname) values (%s, %s, %s, %s)',
			(newName, newPassword, newEmail, newFullname))

		cursor.close()
		dbConnection.close()
		return true

	return false







# Routes goes here

#@app.route('/sayhello')
#def pedro():
#	name = request.args.get('name')
#	return render_template('say.html', name = name)

@app.route('/')
def index():
	print('funciona')
	return render_template('index.html')

@app.route('/register')
def registrar():
	print('funciona')
	return render_template('register.html')

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
		print("el usuario existe en la BD")
		datos = obtenerDatosUsuario(name)
		usuario = datos['fullname']
		print("usuario: "+usuario)
		listPin = searchPin(pageP,name)
		return render_template('lobby.html',error = error, usuario = usuario, listPin = listPin)
	else:
		print("el usuario no existe en la BD")
		error = 'ERROR: Correo electronico o Contrasena son invalidos.'
		return render_template('index.html', error = error, usuario = name)

@app.route('/registeraction', methods = ['POST'])
def registerAction():
	name	 = request.form['name']
	password = request.form['password']
	email	 = request.form['email']
	fullname = request.form['fullname']
	print("Los datos que llegaron al server son "+name+" "+password+" "+email+" "+fullname)
	if(crearCuenta(name, password, email, fullname)):
		listPin = searchPin(pageP,name)
		print('El usuario no existia en la BD, se creo')
		return render_template('lobby.html',usuario = name, listPin = listPin)

	print ('El usuario ya existe %s en la BD', name)
	return render_template('register.html',usuario = name, listPin = listPin)


	

# Routes end here

if __name__ == '__main__':
  app.debug = True
  app.run( host = '0.0.0.0', port = 5000 )

