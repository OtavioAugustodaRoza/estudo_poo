from aula4 import CarinhoDeCompras, Produto

carinho = CarinhoDeCompras()

p1 = Produto('camisa', 10)
p2 = Produto('bone', 60)
p3 = Produto('tenis', 50)

carinho.adicionar_carinho(p1)
carinho.adicionar_carinho(p2)
carinho.adicionar_carinho(p3)

carinho.lista_produtos
print(carinho.soma_total())