from flask import Flask, jsonify

miapp = Flask(__name__)

@miapp.route('/personas', methods=['GET'])

def index():
    lista_usuarios = [
        {'name': 'Joel Orozco'},
        {'name': 'Maria Fernanda Amador'},
        {'name': 'Camila Hernandez'},
        {'name': 'Federico Escobar Garcia'},
        {'name': 'Lilina Hernandez'}
    ]

    return jsonify(lista_usuarios)

if __name__ == '__main__':
    miapp.run(debug=True)