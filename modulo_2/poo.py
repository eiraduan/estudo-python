class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade}"
    
pessoa1 = Pessoa("Saimor", 25)
mensagem = pessoa1.saudacao()
print(mensagem)