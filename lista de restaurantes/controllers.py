from flask import Blueprint, render_template, request, redirect, url_for
from models import restaurantes,addRestaurante, excluir, subs

restaurantes_controller= Blueprint('restaurante', __name__)

@restaurantes_controller.route("/")
def index():
    return render_template('index.html', restaurantes=restaurantes)
@restaurantes_controller.route("/add", methods=['POST'])
def add():
    id=len(restaurantes)+1
    nome=request.form['campo1']
    refeicao=request.form['campo2']
    sobremesa=request.form['campo3']
    localizacao=request.form['campo4']
    addRestaurante(id,nome,refeicao,sobremesa, localizacao)
    return redirect(url_for('restaurante.index'))


@restaurantes_controller.route("/<int:id>", methods=['GET','DELETE'])
def exclu(id):
    x=restaurantes
    excluir(x,id)
    return redirect(url_for('restaurante.index'))
@restaurantes_controller.route("/sub/<int:id>", methods=['POST','PUT'])
def substituir(id):
    valor1 =request.form['valor1']
    valor2 =request.form['valor2']
    valor3 =request.form['valor3']
    valor4 =request.form['valor4']
    subs(id,valor1,valor2,valor3,valor4)
    return redirect(url_for('restaurante.index'))
@restaurantes_controller.route("/subst/<int:id>", methods=['GET'])
def nova(id):
    return render_template('nova.html',id=id)
