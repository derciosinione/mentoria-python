# Ciclos de Repetições
#  - for -> Usamos quando sabemos o numero de vezes que o codigo deve ser executado
#  - while -> Usamos quando nao sabemos o numero de vezes que o codigo deve ser executado

numero = int(input('Informa um numero: '))

for valor in range(0,12):
  valor_real = valor + 1
  print('{}*{}={}'.format(numero,valor_real,(numero*valor_real)))



