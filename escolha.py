nomes = []
equacoes = []
n = int(input())

for i in range(n):
    dados = input().split()
    nome = dados[0]
    nomes.append(nome)
    equacoes.append(2 * int(dados[1]) + 3 * int(dados[2]) + int(dados[3]))

if n==1:
    print(nomes[0])
else:
    eq1 = max(equacoes)
    indicem1 = equacoes.index(eq1)
    nome1 = nomes[indicem1]
    del equacoes[indicem1]
    del nomes[indicem1]

    eq2 = max(equacoes)
    indicem2 = equacoes.index(eq2)
    nome2 = nomes[indicem2]

    result = [nome1,nome2]
    if eq1 == eq2:
        result.sort()

    print (result[0])
    print (result[1])
