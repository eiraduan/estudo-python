from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar():
        pass

    @abstractmethod
    def desligar():
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return "Carro ligado usando a chave"
    
    def desligar(self):
        return "Carro desligado usando a chave"

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())
