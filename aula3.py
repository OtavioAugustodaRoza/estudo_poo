from datetime import datetime

class Transacao:
    def __init__(self,tipo,valor,saldo_resultante):
        self.__tipo = tipo
        self.__valor = valor
        self.__saldo_resultante = saldo_resultante
        self.__data_hora = datetime.now()

    def __str__(self):
     return f"{self.tipo} | R${self.__valor} | {self.__data_hora} | Saldo: {self.__saldo_resultante}"   

    @property
    def tipo(self):
        return self.__tipo

    @property
    def valor(self):
        return self.__valor

    @property
    def data_hora(self):
        return self.__data_hora

    @property
    def saldo_resultante(self):
        return self.__saldo_resultante



class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
        self.__transacoes = []

    def extrato(self):
        for t in self.__transacoes:
            print(t)

    @property
    def transacoes(self):
        return self.__transacoes.copy()
    
    @property 
    def saldo(self):
        return self.__saldo
    
    def sacar(self,valor):
        if valor <= self.__saldo and valor > 0:
            self.__saldo-=valor
            self.__transacoes.append(Transacao("saque",valor,self.__saldo))
        else:
            raise ValueError('valor invalido')    
          
    def depositar(self,valor):
        if valor > 0:
            self.__saldo+=valor
            self.__transacoes.append(Transacao("deposito",valor,self.__saldo))
        else:
            raise ValueError('valor invalido') 
        
    def transferencia(self,valor,destino):
        if self == destino:
           raise ValueError('transacao invalida')
    
        self.sacar(valor)
        destino.depositar(valor)    
            


otavio = ContaBancaria(100)
neymar = ContaBancaria(20000)
neymar.transferencia(2000,otavio)
print(neymar.extrato)