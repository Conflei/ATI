from flask import *
import psycopg2
import os
import app

session = 1


@app.route('/login', methods = ['POST'])
def login():
	print("Los datos que llegaron al server son "+request.form['Name']+" "+request.form['Password'])
	name = request.form['Name']
	password = request.form['Password']
	exist = app.existUser(name=name,password=password)
	error = ""
	if exist:
		print("el usuario existe en la BD")
		datos = app.obtenerDatosUsuario(name)
		usuario = datos['fullname']
		print("usuario: "+usuario)
		listPin = app.searchPin(pageP,name)
		return render_template('lobby.html',error = error, usuario = usuario, listPin = json.dumps(listPin))
	else:
		print("el usuario no existe en la BD")
		error = 'ERROR: Correo electronico o Contrasena son invalidos.'
		return render_template('index.html', error = error, usuario = name)