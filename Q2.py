
def determinar_k():
    n = int(input("Informe o valor para definir a faixa de valores da lista: "))
    lista = []

    valores = {}
    elemento_com_maior_frequencia = []
    maior_frequencia = 0

    limite = 4 * n
    print(f"Os valores que serão adicionados na lista deverão estar no intervalo [{0}, {limite}]")
    for i in range(n):
        valor = int(input("Informe um valor para adicionar a lista: "))

        if valor >= 0 and valor <= limite:
            lista.append(valor)
            if valor in valores:
                valores[valor] += 1
                if valores[valor] == maior_frequencia:
                    elemento_com_maior_frequencia.append(valor)
                elif valores[valor] > maior_frequencia:
                    maior_frequencia = valores[valor]
                    elemento_com_maior_frequencia = [valor]
            else:
                valores[valor] = 1
                if valores[valor] == maior_frequencia:
                    elemento_com_maior_frequencia.append(valor)
                elif valores[valor] > maior_frequencia:
                    maior_frequencia = valores[valor]
                    elemento_com_maior_frequencia = [valor]
        else:
            print("Valor fora da faixa de valores")
            
    if len(elemento_com_maior_frequencia) == len(lista):
        print(f"Todos os valores aprsentam a mesma frequência")

    elif len(elemento_com_maior_frequencia) * maior_frequencia == len(lista):
        print("Todos os valores apresentam a mesma frequência")
        
    else:
        print(f"O(s) valor(es) com maior frequência são {elemento_com_maior_frequencia}, tendo frequência igual a {maior_frequencia}")

determinar_k()
