import random
from Personagem import Personagem

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


def estilo_classico(nome):
    print("\n=== Estilo Clássico ===")
    atributos = {}
    ordem = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

    for atr in ordem:
        resultado, total = lancaDados(3)
        atributos[atr] = sum(resultado)
    
    personagem = Personagem(nome)
    personagem.atribuir(atributos)
    return personagem


def estilo_aventureiro(nome):
    print("\n=== Estilo Aventureiro ===")
    atributos = {}
    ordem = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

    for atr in ordem:
        resultado, total = lancaDados(6)
        # simplificação: média arredondada
        atributos[atr] = round(total / len(resultado))
    
    personagem = Personagem(nome)
    return personagem


def estilo_heroico(nome):
    print("\n=== Estilo Heroico ===")
    atributos = {}
    ordem = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

    for atr in ordem:
        resultado, total = lancaDados(4)
        atributos[atr] = total
    
    personagem = Personagem(nome)
    personagem.atribuir(atributos)
    return personagem