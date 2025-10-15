class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    
    def consultar_saldo(self):
        return self.__saldo
    

conta = ContaBancaria(1000)
print("Saldo:", conta.consultar_saldo())

print("Depositar 1000")
conta.depositar(1000)
print("Saldo:", conta.consultar_saldo())

print("Depositar -100")
conta.depositar(-100)
print("Saldo:", conta.consultar_saldo())

print("Sacar 300")
conta.sacar(300)
print("Saldo:", conta.consultar_saldo())