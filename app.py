from flask import Flask, request, session, g, redirect, abort, render_template, flash

#configuração 
DATABASE = "blog.bd"
SECRET_KEY = 'pudim'

def conectar_bd():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def antes_requisiscao():
    g.bd = conectar_bd()

@app.teardown_request
def depois_request():
    g.bd.close()

@app.route('/')
def exibir_entradas():
    return "Aqui estarão as "
    
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/hello')
def pagina_inicial():
    return "Hello World"