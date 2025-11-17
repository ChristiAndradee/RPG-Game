from Personagem import Personagem
import RolandoAtributos
from Raca import escolher_raca
from Classes import escolher_classe
from utils.json_utils import salvar_personagem   # ou from utils.json_utils import salvar_personagem

def main(): 
    nome = input("Digite seu nome: ")

    print("\nEscolha o estilo de jogo:")
    print("1 - Clássico")
    print("2 - Aventureiro")
    print("3 - Heroico")
    escolha = input("Digite o número do estilo: ")

    if escolha == "1":
        personagem = RolandoAtributos.estilo_classico(nome)
    elif escolha == "2":
        personagem = RolandoAtributos.estilo_aventureiro(nome)
    elif escolha == "3":
        personagem = RolandoAtributos.estilo_heroico(nome)
    else:
        print("Escolha inválida!")
        return
    
    raca_escolhida = escolher_raca()
    classe_escolhida = escolher_classe()

    personagem.set_raca(raca_escolhida.nome)
    personagem.set_classe(classe_escolhida.nome)

    habilidades_totais = raca_escolhida.habilidades + classe_escolhida.habilidades
    personagem.set_habilidades(habilidades_totais)

    print("\n=== Atributos finais do personagem ===")
    personagem.mostrarPersonagem()

    # 🔵 SALVAR EM JSON AQUI (DENTRO DO main)
    salvar_personagem(personagem)

if __name__ == "__main__":
    main()
