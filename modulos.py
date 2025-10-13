# importação padrão
import math

numero = 25
raiz_quadrada = math.sqrt(numero)
print(f"quadrado de {numero} é {raiz_quadrada}")


# importação padrão
from math import sqrt

numero = 25
raiz_quadrada = sqrt(numero)
print(f"quadrado de {numero} é {raiz_quadrada}")

from modulo_personalizado import saudacao

saudacao("Saimor")