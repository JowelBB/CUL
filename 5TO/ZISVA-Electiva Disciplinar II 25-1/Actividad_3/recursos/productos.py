from flask import jsonify, request
import pymysql
import db_config

def get_productos():
    conection = db_config.get_db_connection()
    cursor = conection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    conection.close()
    return jsonify(productos)

def get_producto(id):
    conection = get_db_connection()
    cursor = conection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM productos WHERE id = %s', (id,))
    producto = cursor.fetchone()
    conection.close()
    if producto:
        return jsonify(producto)
    return jsonify({'mensaje': 'Producto no encontrado'}), 404

def create_producto():
    data = request.get_json()
    conection = get_db_connection()
    cursor = conection.cursor()
    cursor.execute('INSERT INTO productos (nombre, descripcion, precio, categoria_id) VALUES (%s, %s, %s, %s)',
                   (data['nombre'], data['descripcion'], data['precio'], data['categoria_id']))
    conection.commit()
    conection.close()
    return jsonify({'mensaje': 'Producto creado'}), 201

def update_producto(id):
    data = request.get_json()
    conection = get_db_connection()
    cursor = conection.cursor()
    cursor.execute('UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, categoria_id = %s WHERE id = %s',
                   (data['nombre'], data['descripcion'], data['precio'], data['categoria_id'], id))
    conection.commit()
    conection.close()
    return jsonify({'mensaje': 'Producto actualizado'})

def delete_producto(id):
    conection = get_db_connection()
    cursor = conection.cursor()
    cursor.execute('DELETE FROM productos WHERE id = %s', (id,))
    conection.commit()
    conection.close()
    return jsonify({'mensaje': 'Producto eliminado'})