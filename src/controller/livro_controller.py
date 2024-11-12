from flask import Blueprint, jsonify

# http://127.0.0.1:5000/

livro_bp = Blueprint('livro', __name__, url_prefix='/livros')

@livro_bp.route('/listar_livros', methods=['GET'])
def listar_livros():
    
    livros = {'titulo': 'Chápeuzinho vermelho e os 40 ladrões', 'autor': 'mauricio de souza', 'url_imagem': 'essa aqui é foto', 'categoria': 'esportes'}
    
    return jsonify(livros) 
    