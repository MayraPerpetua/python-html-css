from flask import Flask, request, session, g, redirect, abort, render_template, flash

#configuração 
DATABASE = "blog.bd"
SECRET_KEY = 'pudim'
app = Flask(__name__)

@app.route('/hello')
def pagina_inicial():
    return "Hello World"