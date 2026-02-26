class Cliente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__enderecos = []

    @property
    def nome(self):
        return self.__nome    
    @property
    def idade(self):
        return self.__idade  

    def lista_enderecos(self):
        for endereco in self.__enderecos:
            print(endereco.estado, endereco.cidade) 

    def adicionar_endereco(self,cidade,estado):
        self.__enderecos.append(Endereco(cidade, estado))


class Endereco:
    def __init__(self, cidade, estado):
        self.estado = estado
        self.cidade = cidade

        




        