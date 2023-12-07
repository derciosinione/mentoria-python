
# def funcao2(x):
#   return len(x)

# l = ['ana', 'paula', 'maria', 'marinho', 'dercio sinione', 'Mario antonio Jose maria']
# saida = max(l, key=lambda x: len(x))

# # print(saida)

# def pessoa(nome, idade):
#   print(f'{nome} - {idade}')
  
  
# n = pessoa("Derone", 12)  

# soma = lambda n1: n1 + 34

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(3)
# print(mydoubler(2))

# pontuacoes = [('Alice', 85), ('Bob', 72), ('Charlie', 90)]
# ordenado_por_pontuacao = sorted(pontuacoes, key= lambda x: x[1], reverse=True)
# print(ordenado_por_pontuacao)

# my_par = [x for x in range(20) if x%2==0]
# my_impar = [x for x in range(20) if x%2!=0]

# l = ['23/05/2022', '23/06/2022', '23/11/2022', '23/09/2022']

# valor = '/'.join(min([d.split('/') for d in l], key=lambda x: int(x[1])))

# print(valor)
# result = '/'.join(max())

def diagonal_principal(matriz):
    # Verifica se a matriz é quadrada
    if len(matriz) != len(matriz[0]):
        return "A matriz não é quadrada, não possui diagonal principal."
    
    # Retorna a diagonal principal como uma lista
    return [matriz[i][i] for i in range(len(matriz)-1, -1, -1)]
    
    # diagonal_principal = []
    # for l in range(2,-1,-1):
    #     diagonal_principal.append(matriz[l][l])
    
    # return diagonal_principal
      

# Exemplo de uso
matriz_exemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal = diagonal_principal(matriz_exemplo)
print("Diagonal Principal:", diagonal)

