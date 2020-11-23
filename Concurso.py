nomes = []
notas = []

def informar_dados():
    for i in range(5):
        nome = input(f"Informe o nome do {i+1}º participante: ")
        nomes.append(nome)
        nota_valida = False
        while not nota_valida:
            nota = float(input(f"Informe a nota do {i+1}º participante: "))
            if nota >= 0 and nota <= 10:
                notas.append(nota)
                nota_valida = True
            else:
                print(f"Nota {nota} inválda, digite um valor entre 0 e 10.")

def nota_mais_alta():
    notaMaisAlta = max(notas)
    i = notas.index(notaMaisAlta)
    nomeVencedor = nomes[i]
    print("-"*40)
    print(f"O(a) vencedor(a) foi {nomeVencedor} com nota {notaMaisAlta}!")

informar_dados()
nota_mais_alta()