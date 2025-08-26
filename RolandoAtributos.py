import random
from Personagem import Personagem

ordem = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

#
def lancaDados(qtdDados):

    atributo = []
    totalDados = 0

    for contador in range(1, qtdDados + 1):
        dado = random.randint(1, 6)
        print(f"Seu {contador}º dado deu {dado} pontos.")
        atributo.append(dado)

    if qtdDados == 3:
        totalDados = sum(atributo)
    else:
        # Substitui o menor valor por 0 
        menor = min(atributo)
        indice = atributo.index(menor)
        atributo[indice] = 0
        totalDados = sum(atributo)

    print("Resultados:", atributo)
    print("Total dos dados:", totalDados,"\n\n")
    return atributo, totalDados

def distribuir_valores(resultados):

    atributos = {}
    print("\nSeus resultados foram:", resultados)

    for atr in ordem:
        while True:
            try:
                escolha = int(input(f"Escolha um valor para {atr}: "))
                if escolha in resultados:
                    atributos[atr] = escolha
                    resultados.remove(escolha)
                    break
                else:
                    print("Valor inválido ou já usado. Tente novamente.")
            except ValueError:
                print("Digite um número válido.")

    return atributos


def estilo_classico(nome):
    print("\n=== Estilo Clássico ===")
    atributos = {}


    for atr in ordem:
        resultado, total = lancaDados(3)
        atributos[atr] = sum(resultado)
    
    personagem = Personagem(nome)
    personagem.atribuir(atributos)
    return personagem


def estilo_aventureiro(nome):
    print("\n=== Estilo Aventureiro ===")
    
    resultados = []
    for _ in range(6):
        resultado, total = lancaDados(3)
        resultados.append(total)

    atributos = distribuir_valores(resultados)
    personagem = Personagem(nome)
    personagem.atribuir(atributos)
    return personagem



def estilo_heroico(nome):
    print("\n=== Estilo Heroico ===")

    # 6 lançamentos de 4 dados
    resultados = []
    for _ in range(6):
        resultado, total = lancaDados(4)
        resultados.append(total)

    atributos = distribuir_valores(resultados)
    personagem = Personagem(nome)
    personagem.atribuir(atributos)
    return personagem