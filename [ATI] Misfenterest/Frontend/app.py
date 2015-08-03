from flask import *
import modelo
import psycopg2
import os

UPLOAD_FOLDER = "models/uploads"

app = Flask (__name__, template_folder = 'views', static_folder = 'statics')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

pageP = 1;



#####################################################################################################################
#modeloo################################################

def existUser (name,password):
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
	cursor.execute('select * from users where name=%s',[name]) 
	tmp = cursor.fetchone()
	datos['fullname'] = tmp[0]

	cursor.close()
	dbConnection.close()

	return datos

def searchPin(pageP,name):
	dbConnection = psycopg2.connect('dbname=atidatabase user=postgres password=123 host=localhost')
	cursor = dbConnection.cursor()
	print("estoy en search pin")

	listPin = []
	cursor.execute('select picdir from pictures offset %s limit 6',[((pageP-1)*7)])
	
	dataPin = cursor.fetchall();
	for dPin in dataPin:
		
		Pin = {}
		Pin['url'] = dPin
		print (Pin['url'])
		listPin.append(Pin)

	cursor.close()
	dbConnection.close()

	return listPin

def crearCuenta (newName, newPassword, newEmail, newFullname):
	if(not existUser(newName, newPassword)):
		dbConnection = psycopg2.connect('dbname=atidatabase user=postgres password=123 host=localhost')
		cursor = dbConnection.cursor()
		cursor.execute('insert into users (name, password, email, fullname) values (%s, %s, %s, %s)',
			(newName, newPassword, newEmail, newFullname))

		dbConnection.commit();
		cursor.close()
		dbConnection.close()
		return True

	return False

def GetImageFilename(category):
	dbConnection = psycopg2.connect('dbname=atidatabase user=postgres password=123 host=localhost')
	cursor = dbConnection.cursor()
	cursor.execute('SELECT COUNT(*) FROM pictures WHERE category = %s', [category])
	(count,) = cursor.fetchone()
	return "picture"+str(count)


# Routes goes here

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
		return render_template('lobby.html',error = error, usuario = usuario, listPin = json.dumps(listPin))
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
	if(crearCuenta(name, password, email, fullname)):
		listPin = searchPin(pageP,name)
		return render_template('lobby.html',usuario = name, listPin = listPin)

	return render_template('register.html',usuario = name, listPin = listPin)
	

@app.route('/uploadcontent', methods = ['POST'])
def loadImage():
	print("Upload Content")
	title 		= request.form['title']
	description = request.form['description']
	imageData 	= request.files['file'];
	name = imageData.filename
	ext = name.rsplit('.', 1)[1]
	filename = GetImageFilename('upload')+ext
	print("El nombre de esta imagen sera "+filename)
	imageData.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

	return render_template('lobby.html')



	

# Routes end here

if __name__ == '__main__':
  app.debug = True
  app.run( host = '0.0.0.0', port = 5000 )

