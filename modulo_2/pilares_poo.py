class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")
        return
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au, Au!"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    
dog = Cachorro(nome="Fred")
cat = Gato(nome="Nani")

animais = [dog, cat]

for animal in animais:
    print(f"Meu nome é {animal.nome} e faço {animal.emitir_som()}")