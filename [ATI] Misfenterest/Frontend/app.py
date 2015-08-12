from flask import *
from flask.ext.bcrypt import Bcrypt
import modelo
import psycopg2
import os

class User:
	def __init__(self, name, fullname, picDir, description, email):
		self.name 		 = name
		self.fullname    = fullname
		self.picdir		 = picDir
		self.description = description
		self.email 		 = email

UPLOAD_FOLDER = "models/uploads"

app = Flask (__name__, template_folder = 'views', static_folder = 'statics')
bcrypt = Bcrypt(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#####################################################################################################################
#modeloo################################################

def existUser (name,password):
	dbConnection = psycopg2.connect('dbname=atidatabase user=postgres password=123 host=localhost')
	cursor = dbConnection.cursor()

	cursor.execute('select password from users where name=%s',[name])

	print("executed")
	if cursor.rowcount == 0:
		cursor.close()
		dbConnection.close()
		print("not founded user with this nickname")
		return False
	else:
		(dbPassword,) = cursor.fetchone()
		check = bcrypt.check_password_hash(dbPassword, password)
		cursor.close()
		dbConnection.close()

	if check:
		print("ACCEPTED")
		return True
	else:
		print("WRONG PASSWORD")
	return False

def obtenerDatosUsuario(name):

	dbConnection = psycopg2.connect('dbname=atidatabase user=postgres password=123 host=localhost')
	cursor = dbConnection.cursor()

	datos = {}
	cursor.execute('select * from users where name=%s',[name])
	tmp = cursor.fetchone()

	user = User(tmp[0], tmp[4], tmp[2], tmp[5], tmp[3])
	print("Obtenidos los datos de un usuario")
	print("Nickname: "+user.name)
	print("Fullname: "+user.fullname)
	print("picDir: "+user.picdir)
	print("Description: "+str(user.description))
	print("Email: "+user.email)

	cursor.close()
	dbConnection.close()

	return user

def searchPin(page,type,username): #retorna 5 imagenes en formato json
	dbConnection = psycopg2.connect('dbname=atidatabase user=postgres password=123 host=localhost')
	cursor = dbConnection.cursor()
	cursor2 = dbConnection.cursor()
	print("estoy en search pin")
	if type == 'all':
		cursor.execute('select * from pictures offset %s limit %s',(page,5))
	else:
		if type == 'upload':
			cursor.execute('select * from pictures offset %s limit %s',(page,5)) #comentar cuando todo este bien
			#cursor.execute('select * from pictures where author =%s offset %s limit %s',(name,page,5))
		else:
			if type == 'pin':
				cursor.execute('select p.* from pictures p, pin pi where p.picdir = pi.picdir offset %s limit %s',(page,5))

	dataPin = cursor.fetchall()

	print("user namee "+str(username))

	cursor2.execute('select * from pin where name=%s',(username,))
	dataPin2 = cursor2.fetchall()
	print(dataPin2)

	dataJSON = ""
	imgJSON = ""
	i = 0
	pin = "False"

	for dPin in dataPin:
		print("Soy Pin 1 "+dPin[0]) #imagen en pictures
		if type != 'pin':
			for dPin2 in dataPin2:
				print("Soy Pin 2 "+dPin2[1]) #imagen pineada
				if dPin[0] == dPin2[1]:
					pin = "True"
					break
		else:
			pin = "False";
		print("holaaaaa11111")
		imgJSON = "{\"picdir\":\""+str(dPin[0])+"\",\"title\":\""+str(dPin[1])+"\",\"category\":\""+str(dPin[2])+"\",\"description\":\""+str(dPin[3])+"\",\"author\":\""+str(dPin[4])+"\",\"isPin\":\""+pin+"\"}"
		print("holaaaaa22222")
		pin = "False"
		if dataJSON == "":
			dataJSON = "[" + imgJSON
		else:
			dataJSON = dataJSON + "," + imgJSON
	if dataJSON != "":
		dataJSON = dataJSON + "]"
	else:
		dataJSON = "[]"

	dbConnection.commit()
	cursor.close()
	cursor2.close()
	dbConnection.close()
	print("enviare pines: "+dataJSON)
	return dataJSON

def crearCuenta (newName, newPassword, newEmail, newFullname):
	if(not existUser(newName, newPassword)):
		dbConnection = psycopg2.connect('dbname=atidatabase user=postgres password=123 host=localhost')
		cursor = dbConnection.cursor()
		pw_hash = bcrypt.generate_password_hash(newPassword)
		cursor.execute('insert into users (name, password, email, fullname) values (%s, %s, %s, %s)',
			(newName, pw_hash, newEmail, newFullname))

		dbConnection.commit()
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

	dbConnection.commit()
	cursor.close()
	dbConnection.close()
	return True

def EditPerfilInDB(name,fullname,userAbout,img):#,cargarImagen): #usuario,nombrecompleto,descripcion,fotoperfil
	dbConnection = psycopg2.connect('dbname=atidatabase user=postgres password=123 host=localhost')
	cursor = dbConnection.cursor()
	cursor.execute('UPDATE users SET fullname  = %s WHERE name = %s',(fullname, name))
	cursor.execute('UPDATE users SET description  = %s WHERE name = %s',(userAbout, name))
	if img != 'none':
		cursor.execute('UPDATE users SET picdir  = %s WHERE name = %s',(img, name))
	dbConnection.commit()
	cursor.close()
	dbConnection.close()
	return "exito"

def pinInDB(name,picdir,tipo):
	dbConnection = psycopg2.connect('dbname=atidatabase user=postgres password=123 host=localhost')
	cursor = dbConnection.cursor()
	if tipo == 'pin':
		cursor.execute('insert into pin (name, picdir) values (%s, %s)',(name, picdir))
	else:
		cursor.execute('delete from pin where name = %s and picdir = %s',(name, picdir))
	dbConnection.commit()
	cursor.close()
	dbConnection.close()
	return "exito"


######################################FIN MODELO###################################
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

@app.route('/font/<path:path>')
def send_font(path):
	return send_from_directory('font', path)



@app.route('/assets/<path:path>')
def send_assets(path):
	return send_from_directory('assets', path)

@app.route('/fonts/<path:path>')
def send_fonts(path):
	return send_from_directory('fonts', path)

@app.route('/models/uploads/<path:path>')
def send_up(path):
	return send_from_directory('models/uploads', path)

@app.route('/FacebookLogin', methods = ['POST'])
def FacebookLogin():
	print("Alguien se logeo con Facebook y su nombre es "+ request.form['name'])
	username = request.form['name']
	password = request.form['password']

	if existUser(name=name,password=password):
		print("el usuario existe en la BD")
		datos = obtenerDatosUsuario(name)
		usuario = datos.name
		print("usuario: "+usuario)
		#listPin = searchPin(pageP,name,0)
		print('Sending user '+usuario)
		return render_template('lobby.html',error = error, usuario = datos)
	else:
		print('Este usuario no existe en la BD, se esta creando')
		email	 = 'emailfromfacebook@email.com'
		fullname = request.form['name']
		if(crearCuenta(username, password, email, fullname)):
			return render_template('lobby.html',usuario = name)#, listPin = listPin)

	return render_template('register.html',usuario = name)



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
		usuario = datos.name
		print("usuario: "+usuario)
		#listPin = searchPin(pageP,name,0)
		print('Sending user '+usuario)
		return render_template('lobby.html',error = error, usuario = datos)#, listPin = json.dumps(listPin))
	else:
		print("el usuario no existe en la BD")
		error = 'ERROR: Correo electronico o Contrasena son invalidos.'
		return render_template('index.html', error = error, usuario = name)


@app.route('/verLobby', methods = ['POST'])
def verLobby():
	name = request.form['Name']
	datos = obtenerDatosUsuario(name)
	usuario = datos.name
	print("usuario: "+usuario)
	return render_template('lobby.html',usuario = datos)#, listPin = json.dumps(listPin))


@app.route('/registeraction', methods = ['POST'])
def registerAction():
	name	 = request.form['name']
	password = request.form['password']
	email	 = request.form['email']
	fullname = request.form['fullname']
	if(crearCuenta(name, password, email, fullname)):
		#listPin = searchPin(pageP,name,0)
		return render_template('lobby.html',usuario = name)#, listPin = listPin)

	return render_template('register.html',usuario = name)#, listPin = listPin)


@app.route('/myprofile', methods = ['POST'])
def myProfile():
	print("My profile")
	nickname = request.form['name']
	user = obtenerDatosUsuario(nickname)
	return render_template('perfil.html', usuario = user)

@app.route('/get_image_json', methods = ['GET'])
def get_image_json(): #funcion llamada por el ajax para paginar

	page = request.args.get('page')
	type = request.args.get('type')
	username = request.args.get('username')
	print("Paginando"+str(page))
	return searchPin(page,type,username) #retorna json con 5 imagenes

@app.route('/uploadcontent', methods = ['POST'])
def loadImage():
	print("Upload Content")
	title 		= request.form['title']
	description = request.form['description']
	imageData 	= request.files['file']
	author 		= request.form['author']
	name = imageData.filename
	ext = name.rsplit('.', 1)[1]
	filename = GetImageFilename('upload')+"."+ext.lower()
	finalPath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
	imageData.save(finalPath)
	print("La imagen fisica se guardo en el server en la ruta "+finalPath)
	NewPicture(finalPath, title, "upload", description, author)
	print("La imagen se guardo en la BD")

	user = obtenerDatosUsuario(author)
	return render_template('lobby.html', usuario = user)

@app.route('/EditPerfil', methods = ['GET'])
def EditPerfil(): #funcion llamada por el ajax para Editar Perfil
	name = request.args.get('name')
	fullname = request.args.get('fullname')
	userAbout = request.args.get('userAbout')
	img = 'none'
	print("Estoy en editar Perfil")
	print(str(name)+" "+str(fullname)+" "+str(userAbout))#+" "+str(finalPath))
	return EditPerfilInDB(name,fullname,userAbout,img)#,finalPath) #retorna mensaje 'exito' si todo sale bien, 'fallo' en otro caso


@app.route('/editarPerfilForm', methods = ['POST'])
def editarPerfilForm():

	nameUsr 	= request.form['name']
	fname 		= request.form['fname']
	description = request.form['about']
	imageData 	= request.files['file']

	name = imageData.filename
	ext = name.rsplit('.', 1)[1]
	filename = GetImageFilename('upload')+"."+ext.lower()
	finalPath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
	imageData.save(finalPath)
	print("Ya guarde la imagen estos son los datos %s %s %s",nameUsr, fname,description,finalPath)
	EditPerfilInDB(nameUsr,fname,description,finalPath)

	user = obtenerDatosUsuario(nameUsr)

	return render_template('perfil.html', usuario = user)


@app.route('/pin', methods = ['GET']) #HACE PIN A UNA FOTO, O QUITA PIN A UNA FOTO
def pin():
	name = request.args.get('name')
	picdir = request.args.get('picdir')
	tipo = request.args.get('tipo')
	print("holaaaaaaaa"+str(name)+" hace "+str(tipo)+" a la imagen: "+str(picdir))
	return pinInDB(name,picdir,tipo)

# Routes end here

if __name__ == '__main__':
  app.debug = True
  app.run( host = '0.0.0.0', port = 5000 )
