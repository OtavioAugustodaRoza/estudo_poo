class CarinhoDeCompras:
    def __init__(self):
        self.__produtos = []

    @property
    def lista_produtos(self):
        for produto in self.__produtos:
            print(produto.nome, produto.valor)
        

    def adicionar_carinho(self, produto):
        self.__produtos.append(produto)

    def soma_total(self):
        total = 0
        for produto in self.__produtos:
            total += produto.valor
        return total    
            
class Produto:
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome
    
    @property
    def valor(self):
        return self.__valor