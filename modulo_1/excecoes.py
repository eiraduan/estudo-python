try:
    numero = int(input("Digite um numero: "))
    resultado = 10 / numero
except ValueError as e:
    print(f"Erro de valor {e}")
    raise ValueError("Tipo de variaveis incompativeis")
except Exception as e:
    print(f"Erro exceção {e}")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Operacao finalizada")