combinacoes = []
n = int(input())
cont = 0

for direita in range(0,6):
    for esquerda in range(0,6):
       if(direita + esquerda == n) and[esquerda,direita] not in combinacoes:
            combinacoes.append([direita,esquerda])
            cont +=1
print(cont)