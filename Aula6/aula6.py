
class pessoa: #super classe
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.nomeclass = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclass} esta falando...')    

    @property
    def nome(self):
        return self.__nome    
    @property
    def idade(self):
        return self.__idade  

#sub classes
class Aluno(pessoa):
    pass

class Cliente(pessoa):
    pass
