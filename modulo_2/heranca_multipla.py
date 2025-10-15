class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som():
        pass

class Mamifero(Animal):
    def amamentando(self):
        return f"{self.nome} está AMAMENTANDO"
    
class Ave(Animal):
    def voando(self):
        return f"{self.nome} está VOANDO"
    
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return "Morcegos emitem sons ultrassônicos"
    
morcego = Morcego(nome="Batman")

#Animal
print("Nome do morcego:", morcego.nome)
print("Som do morcego:", morcego.emitir_som())

# Mamifero e Ave
print("Morcego amamentando:", morcego.amamentando())
print("Morcego voando:", morcego.voando())    
