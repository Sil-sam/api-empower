
## CONSTRUIR INSTANCIAS DE BIBLIOTECAS

## INICIAÇÃO DO BANCO DE DADOS, DO FLASK E O REGISTRO DAS BLUEPRINTS

## BLUEPRINT LIVROS 
## BLUEPRINT USUARIOS

from flask import Flask
from src.controller.livro_controller import livro_bp

def create_app():
    
    ## CARREGA AS FUNCIONALIDADES DO FLASK
    app = Flask(__name__)
    app.register_blueprint(livro_bp)
    
    return app 
