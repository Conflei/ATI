import psycopg2



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
