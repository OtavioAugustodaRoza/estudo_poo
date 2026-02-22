from random import randint
class Pessoa:
    ano_atual = 2025
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'{self.nome} - {self.idade}'
        

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod # usar quando o metodo seja referente a classe e não a instancia
    def por_ano_nascimento(cls,ano):
        return cls.ano_atual - ano
    

    @staticmethod 
    def gera_id(): # você pode usar o static quando voce vai fazer apenas uma func normal sem receber instancia nem classe 
        return randint(1000,1999)


    

        