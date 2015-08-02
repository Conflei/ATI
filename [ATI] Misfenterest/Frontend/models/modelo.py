import psycopg2
try:
    connection = psycopg2.connect('dbname=pastie_db user=pastie_usr password=12345 host=localhost')
except:
    print ("I am unable to connect to the database")

def crearUsuario (user,email, password):

	dbConnection = psycopg2.connect('dbname=pastie_db user=pastie_usr password=12345 host=localhost')
	cursor = dbConnection.cursor()
	cursor.execute('select codUsuario from usuario where email=%s',(email,))
	
	if cursor.rowcount > 0:
		return False

	cursor.execute('insert into usuario (nombre,email,clave,fechacreacion,fechaultimoacceso) values (%s,%s,%s,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP)',
		(user,email,password))

	dbConnection.commit()
	cursor.close()
	dbConnection.close()

	return True

def obtenerCodUsuario (email, password):

	dbConnection = psycopg2.connect('dbname=atidatabase user=ati password=123 host=localhost')
	cursor = dbConnection.cursor()

	cursor.execute('select name from users where email=%s and password=%s',(email,password))

	if cursor.rowcount == 0:
		return False

	codUsuario = cursor.fetchone()[0]

	cursor.close()
	dbConnection.close()

	return codUsuario
	
def obtenerCodUsuarioEmail (email):

	dbConnection = psycopg2.connect('dbname=pastie_db user=pastie_usr password=12345 host=localhost')
	cursor = dbConnection.cursor()

	cursor.execute('select codUsuario from usuario where email=%s',(email,))

	if cursor.rowcount == 0:
		return False

	codUsuario = cursor.fetchone()[0]

	cursor.close()
	dbConnection.close()

	return codUsuario

def  obtenerDatosUsuario (codUsuario):
	dbConnection = psycopg2.connect('dbname=atidatabase user=ati password=123 host=localhost')
	cursor = dbConnection.cursor()

	datos = {}
	cursor.execute('select name,email from usuario where name=%s',(codUsuario))

	tmp = cursor.fetchone()
	datos['name'] = tmp[0]
	datos['email'] = tmp[1]

	cursor.close()
	dbConnection.close()

	return datos
	


def cambiarClave (codUsuario, clave):
	dbConnection = psycopg2.connect('dbname=pastie_db user=pastie_usr password=12345 host=localhost')
	cursor = dbConnection.cursor()

	cursor.execute('update usuario set clave=%s where codUsuario=%s',(clave,codUsuario,))
	dbConnection.commit()

	cursor.close()
	dbConnection.close()

def insertarPastie(codUsuario,titulo,contenido,tags,privacidad):

	dbConnection = psycopg2.connect('dbname=pastie_db user=pastie_usr password=12345 host=localhost')
	cursor = dbConnection.cursor()

	listaTags = tags.split(",")

	cursor.execute('insert into pastie (titulo,contenido,nivelPrivacidad,fechaCreacion,fechaUltimaEdicion,codUsuario) values (%s,%s,%s,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP,%s) \
		RETURNING codPastie'
		,(titulo,contenido,privacidad,codUsuario))

	codPastie = cursor.fetchone()[0]

	dbConnection.commit()

	for hashtag in listaTags:

		codCategoria = None
		cursor.execute('select codCategoria from categoria where hashtag=%s',(hashtag,))

		if cursor.rowcount > 0:
			codCategoria = cursor.fetchone()[0]
		else:
			cursor.execute('insert into categoria (hashtag) values (%s) returning codCategoria',(hashtag,))
			codCategoria = cursor.fetchone()[0]		
			dbConnection.commit()

		cursor.execute('insert into asociado (codCategoria,codPastie) values (%s,%s)',(codCategoria,codPastie,))
		dbConnection.commit()

	cursor.close()
	dbConnection.close()

def leerPastie (codPastie, codUsuario):

	dbConnection = psycopg2.connect('dbname=pastie_db user=pastie_usr password=12345 host=localhost')
	cursor = dbConnection.cursor()

	cursor.execute('select p.codPastie,p.titulo, p.contenido, \
			DATE_PART(\'day\',CURRENT_TIMESTAMP-p.fechaUltimaEdicion), DATE_PART(\'hour\',CURRENT_TIMESTAMP-p.fechaUltimaEdicion), \
			DATE_PART(\'minute\',CURRENT_TIMESTAMP-p.fechaUltimaEdicion), p.codUsuario, u.nombre \
			from pastie p, usuario u where p.codPastie=%s and p.codUsuario = u.codUsuario',(codPastie,))

	if cursor.rowcount == 0:
		return None

	pastie = cursor.fetchone()

	cursor.execute('select c.hashtag from categoria c, asociado a where c.codCategoria = a.codCategoria and \
		a.codPastie = %s',(pastie[0],))

	categorias = []
	for cat in cursor:
		categorias.append(cat[0])

	dictPastie = {}
	dictPastie['pastie-id'] = pastie[0]
	dictPastie['pastie-title'] = pastie[1]
	dictPastie['pastie-content'] = pastie[2]
	dictPastie['pastie-cat'] = ','.join(categorias)

	dias = int(pastie[3])
	horas = int(pastie[4])
	minutos = int(pastie[5])

	tiempo = "Hace"

	if dias > 0:
		tiempo += " " + str(dias) + " dias"

	if horas > 0:
		tiempo += " " + str(horas) + " horas"

	if (dias > 0) or (horas > 0):
		tiempo += " y " + str(minutos) + " minutos."
	else:
		tiempo += " " + str(minutos) + " minutos."

	dictPastie['pastie-time'] = tiempo	
	dictPastie['pastie-editable'] = pastie[6] == codUsuario
	dictPastie['pastie-owner'] = pastie[7]

	cursor.close()
	dbConnection.close()

	return dictPastie

def leerPasties (pagina, privado, codUsuario):

	dbConnection = psycopg2.connect('dbname=pastie_db user=pastie_usr password=12345 host=localhost')
	cursor = dbConnection.cursor()

	listaPasties = []

	if privado == False:
		cursor.execute('select p.codPastie,p.titulo, substring(p.contenido for 250), \
			DATE_PART(\'day\',CURRENT_TIMESTAMP-p.fechaUltimaEdicion), DATE_PART(\'hour\',CURRENT_TIMESTAMP-p.fechaUltimaEdicion), \
			DATE_PART(\'minute\',CURRENT_TIMESTAMP-p.fechaUltimaEdicion) , u.nombre \
			from pastie p, usuario u where p.nivelPrivacidad=%s and p.codUsuario = u.codUsuario order by p.fechaUltimaEdicion desc offset %s limit 5',(privado,(pagina-1)*5))
	else:
		cursor.execute('select p.codPastie,p.titulo, substring(p.contenido for 250), \
			DATE_PART(\'day\',CURRENT_TIMESTAMP-p.fechaUltimaEdicion), DATE_PART(\'hour\',CURRENT_TIMESTAMP-p.fechaUltimaEdicion), \
			DATE_PART(\'minute\',CURRENT_TIMESTAMP-p.fechaUltimaEdicion), u.nombre \
			from pastie p, usuario u where p.codUsuario=%s and p.codUsuario = u.codUsuario order by p.fechaUltimaEdicion desc offset %s limit 5',(codUsuario,(pagina-1)*5))

	datosPasties = cursor.fetchall()

	for pastie in datosPasties:

		cursor.execute('select c.hashtag from categoria c, asociado a where c.codCategoria = a.codCategoria and \
			a.codPastie = %s',(pastie[0],))

		categorias = []
		for cat in cursor:
			categorias.append(cat[0])

		dictPastie = {}
		dictPastie['pastie-id'] = pastie[0]
		dictPastie['pastie-title'] = pastie[1]
		dictPastie['pastie-content'] = pastie[2]
		dictPastie['pastie-cat'] = ','.join(categorias)

		dias = int(pastie[3])
		horas = int(pastie[4])
		minutos = int(pastie[5])

		tiempo = "Hace"

		if dias > 0:
			tiempo += " " + str(dias) + " dias"

		if horas > 0:
			tiempo += " " + str(horas) + " horas"

		if (dias > 0) or (horas > 0):
			tiempo += " y " + str(minutos) + " minutos."
		else:
			tiempo += " " + str(minutos) + " minutos."

		dictPastie['pastie-time'] = tiempo
		dictPastie['pastie-owner'] = pastie[6]

		listaPasties.append(dictPastie)		

	cursor.close()
	dbConnection.close()

	return listaPasties

def buscarPasties (tags, pagina):
	listaPasties = []

	dbConnection = psycopg2.connect('dbname=pastie_db user=pastie_usr password=12345 host=localhost')
	cursor = dbConnection.cursor()

	hashtags = tuple(tags.split(','))
	cursor.execute('select p.codPastie,p.titulo, substring(p.contenido for 250), \
		DATE_PART(\'day\',CURRENT_TIMESTAMP-p.fechaUltimaEdicion), DATE_PART(\'hour\',CURRENT_TIMESTAMP-p.fechaUltimaEdicion), \
		DATE_PART(\'minute\',CURRENT_TIMESTAMP-p.fechaUltimaEdicion), u.nombre \
		from pastie p, categoria c, asociado a, usuario u \
		where c.hashtag in %s and c.codCategoria = a.codCategoria and a.codPastie = p.codPastie and p.nivelPrivacidad=False \
		p.codUsuario = u.codUsuario order by p.fechaUltimaEdicion desc offset %s limit 5', (hashtags,(pagina-1)*5))

	datosPasties = cursor.fetchall()

	for pastie in datosPasties:

		cursor.execute('select c.hashtag from categoria c, asociado a where c.codCategoria = a.codCategoria and \
			a.codPastie = %s',(pastie[0],))

		categorias = []
		for cat in cursor:
			categorias.append(cat[0])

		dictPastie = {}
		dictPastie['pastie-id'] = pastie[0]
		dictPastie['pastie-title'] = pastie[1]
		dictPastie['pastie-content'] = pastie[2]
		dictPastie['pastie-cat'] = ','.join(categorias)

		dias = int(pastie[3])
		horas = int(pastie[4])
		minutos = int(pastie[5])

		tiempo = "Hace"

		if dias > 0:
			tiempo += " " + str(dias) + " dias"

		if horas > 0:
			tiempo += " " + str(horas) + " horas"

		if (dias > 0) or (horas > 0):
			tiempo += " y " + str(minutos) + " minutos."
		else:
			tiempo += " " + str(minutos) + " minutos."

		dictPastie['pastie-time'] = tiempo
		dictPastie['pastie-owner'] = pastie[6]

		listaPasties.append(dictPastie)	

	cursor.close()
	dbConnection.close()

	return listaPasties

def eliminarPastie(codPastie,codUsuario):
	dbConnection = psycopg2.connect('dbname=pastie_db user=pastie_usr password=12345 host=localhost')
	cursor = dbConnection.cursor()

	cursor.execute('select from pastie where codPastie=%s and codUsuario = %s',(codPastie,codUsuario,))

	if cursor.rowcount > 0:
		cursor.execute('delete from asociado where codPastie=%s',(codPastie,))
		cursor.execute('delete from pastie where codPastie=%s and codUsuario=%s',(codPastie,codUsuario))
		dbConnection.commit()

	cursor.close()
	dbConnection.close()

def editarPastie (codPastie, titulo, contenido, tags, privacidad, codUsuario):
	dbConnection = psycopg2.connect('dbname=pastie_db user=pastie_usr password=12345 host=localhost')
	cursor = dbConnection.cursor()

	cursor.execute('select codPastie from pastie where codPastie=%s and codUsuario = %s',(codPastie,codUsuario,))

	if cursor.rowcount > 0:
		cursor.execute('delete from asociado where codPastie = %s',(codPastie,))
		cursor.execute('update pastie set titulo=%s,contenido=%s,nivelPrivacidad=%s,fechaUltimaEdicion=CURRENT_TIMESTAMP \
			where codPastie=%s and codUsuario=%s',(titulo,contenido,privacidad,codPastie,codUsuario,))
		
		dbConnection.commit()

		listaTags = tags.split(',')
		for hashtag in listaTags:

			codCategoria = None
			cursor.execute('select codCategoria from categoria where hashtag=%s',(hashtag,))

			if cursor.rowcount > 0:
				codCategoria = cursor.fetchone()[0]
			else:
				cursor.execute('insert into categoria (hashtag) values (%s) returning codCategoria',(hashtag,))
				codCategoria = cursor.fetchone()[0]		
				dbConnection.commit()

			cursor.execute('insert into asociado (codCategoria,codPastie) values (%s,%s)',(codCategoria,codPastie,))
			dbConnection.commit()

	cursor.close()
	dbConnection.close()
