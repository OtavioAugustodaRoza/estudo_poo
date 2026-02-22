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
    

    

        