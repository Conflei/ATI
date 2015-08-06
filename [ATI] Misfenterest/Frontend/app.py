from flask import *
import modelo
import psycopg2
import os
import session

UPLOAD_FOLDER = "models/uploads"

app = Flask (__name__, template_folder = 'views', static_folder = 'statics')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

pageP = 1;
app.secure_key = os.urandom(24)



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
	cursor.execute('select * from pictures where category = upload')
	
	dataPin = cursor.fetchall();
	for dPin in dataPin:
		listPin.append(dPin)

	cursor.close()
	dbConnection.close()
	print("enviare pines: "+str(len(listPin)))
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

def NewPicture(picDir, title, category, description, author):
	dbConnection = psycopg2.connect('dbname=atidatabase user=postgres password=123 host=localhost')
	cursor = dbConnection.cursor()
	cursor.execute('insert into pictures (picdir, title, category, description, author) values (%s, %s, %s, %s, %s)',
			(picDir, title, category, description, author))

	dbConnection.commit();
	cursor.close()
	dbConnection.close()
	return True



# Routes goes here

@app.route('/')
def index():
	print('funciona y la sesion es '+str(session.session))
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
	filename = GetImageFilename('upload')+"."+ext.lower()
	finalPath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
	imageData.save(finalPath)
	print("La imagen fisica se guardo en el server en la ruta "+finalPath)
	NewPicture(finalPath, title, "upload", description, "conflei")
	print("La imagen se guardo en la BD")

	return render_template('lobby.html')



	

# Routes end here

if __name__ == '__main__':
  app.debug = True
  app.run( host = '0.0.0.0', port = 5000 )

