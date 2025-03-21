from flask import Flask, jsonify
from recursos import productos, categorias

app = Flask(__name__)

# Rutas para productos
@app.route('/productos', methods=['GET'])
def get_productos():
    try:
        return productos.get_productos()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/productos/<int:id>', methods=['GET'])
def get_producto(id):
    try:
        return productos.get_producto(id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/productos', methods=['POST'])
def create_producto():
    try:
        return productos.create_producto()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/productos/<int:id>', methods=['PUT'])
def update_producto(id):
    try:
        return productos.update_producto(id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/productos/<int:id>', methods=['DELETE'])
def delete_producto(id):
    try:
        return productos.delete_producto(id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rutas para categorías
@app.route('/categorias', methods=['GET'])
def get_categorias():
    try:
        return categorias.get_categorias()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/categorias/<int:id>', methods=['GET'])
def get_categoria(id):
    try:
        return categorias.get_categoria(id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/categorias', methods=['POST'])
def create_categoria():
    try:
        return categorias.create_categoria()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/categorias/<int:id>', methods=['PUT'])
def update_categoria(id):
    try:
        return categorias.update_categoria(id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/categorias/<int:id>', methods=['DELETE'])
def delete_categoria(id):
    try:
        return categorias.delete_categoria(id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)