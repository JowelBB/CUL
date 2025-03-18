import  pymysql

# Configuracion de la base de datos.
db_config = {
    'host': 'Localhost', 
    'user': 'root',
    'password': 'admin',
    'database': 'mi_api'
}

# Conexion a la base de datos.
def get_db_connection():
    return pymysql.connect(**db_config)