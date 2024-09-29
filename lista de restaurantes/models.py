class Restaurante:
    def __init__(self,id,nome, refeicao, sobremesa, localizacao):
        self.id= id
        self.nome = nome
        self.refeicao=refeicao
        self.sobremesa=sobremesa
        self.localizacao=localizacao
        
restaurantes=[]

def addRestaurante(id,nome,refeicao, sobremesa, localizacao):
    novo_restaurante=Restaurante(id,nome,refeicao,sobremesa,localizacao)
    restaurantes.append(novo_restaurante)
def excluir(restaurantes,banana):
    for restaurante in restaurantes:
        if (restaurante.id == banana):
            restaurantes.remove(restaurante)
            return
def subs(id,valor1,valor2,valor3,valor4):
    for restaurante in restaurantes:
        if (restaurante.id == id):
            restaurante.nome=valor1
            restaurante.refeicao=valor2
            restaurante.sobremesa=valor3
            restaurante.localizacao=valor4
            
