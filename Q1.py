# Até o momento a complexidade da função que faz a verificaçõa é de O(n²)

def verificar(lista):
    somas = set()
    somas.add(lista[0] + lista[1])
    for i in range(2, len(lista)):
        if lista[i] in somas:
            return "Existe um elemento que é a soma de dois anteriores"
        else:
            for j in range(i):
                somas.add(lista[i] + lista[j])
    return "Nehnhum elemento é a soma de dois anteriores"

lista = []
n = int(input("Quantos valores terá a lista? "))

for i in range(n):
    lista.append(int(input("Qual valor vc quer adicionar a lista? ")))

print(verificar(lista))
