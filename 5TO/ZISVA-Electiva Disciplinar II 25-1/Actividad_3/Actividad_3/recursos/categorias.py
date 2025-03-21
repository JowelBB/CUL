from flask import jsonify, request
import pymysql
import db_config
def get_categorias():
    conection = db_config.get_db_connection()
    cursor = conection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM categorias')
    categorias = cursor.fetchall()
    conection.close()
    return jsonify(categorias)

def get_categoria(id):
    conection = db_config.get_db_connection()
    cursor = conection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM categorias WHERE id = %s', (id,))
    categoria = cursor.fetchone()
    conection.close()
    if categoria:
        return jsonify(categoria)
    return jsonify({'mensaje': 'Categoría no encontrada'}), 404

def create_categoria():
    data = request.get_json()
    conection = db_config.get_db_connection()
    cursor = conection.cursor()
    cursor.execute('INSERT INTO categorias (nombre) VALUES (%s)', (data['nombre'],))
    conection.commit()
    conection.close()
    return jsonify({'mensaje': 'Categoría creada'}), 201

def update_categoria(id):
    data = request.get_json()
    conection = db_config.get_db_connection()
    cursor = conection.cursor()
    cursor.execute('UPDATE categorias SET nombre = %s WHERE id = %s', (data['nombre'], id))
    conection.commit()
    conection.close()
    return jsonify({'mensaje': 'Categoría actualizada'}), 200

def delete_categoria(id):
    conection = db_config.get_db_connection()
    cursor = conection.cursor()
    cursor.execute('DELETE FROM categorias WHERE id = %s', (id,))
    conection.commit()
    conection.close()
    return jsonify({'mensaje': 'Categoría eliminada'}), 200