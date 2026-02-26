from aula5 import Endereco, Cliente

neymar = Cliente('neymar', 34)
neymar.adicionar_endereco('joinville' , 'sc')
neymar.adicionar_endereco('santos' , 'sp')

neymar.lista_enderecos()
print(neymar.nome)
print(neymar.idade)
