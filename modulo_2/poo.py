class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def apresentacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade}"


pessoa1 = Pessoa("Saimor", 23)
pessoa2 = Pessoa("Raduan", 25)

mensagem = pessoa1.apresentacao()
print(mensagem)

mensagem2 = pessoa2.apresentacao()
print(mensagem2)

