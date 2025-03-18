from flask import Flask
from recursos import productos, categorias

app = Flask(__name__)

# Rutas para productos
@app.route('/productos', methods=['GET'])
def get_productos():
    return productos.get_productos()

@app.route('/productos/<int:id>', methods=['GET'])
def get_producto(id):
    return productos.get_producto(id)

@app.route('/productos', methods=['POST'])
def create_producto():
    return productos.create_producto()

@app.route('/productos/<int:id>', methods=['PUT'])
def update_producto(id):
    return productos.update_producto(id)

@app.route('/productos/<int:id>', methods=['DELETE'])
def delete_producto(id):
    return productos.delete_producto(id)

# Rutas para categorías
@app.route('/categorias', methods=['GET'])
def get_categorias():
    return categorias.get_categorias()

@app.route('/categorias/<int:id>', methods=['GET'])
def get_categoria(id):
    return categorias.get_categoria(id)

@app.route('/categorias', methods=['POST'])
def create_categoria():
    return categorias.create_categoria()

@app.route('/categorias/<int:id>', methods=['PUT'])
def update_categoria(id):
    return categorias.update_categoria(id)

@app.route('/categorias/<int:id>', methods=['DELETE'])
def delete_categoria(id):
    return categorias.delete_categoria(id)

if __name__ == '__main__':
    app.run(debug=True)