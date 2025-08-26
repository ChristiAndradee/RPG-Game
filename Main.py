from Personagem import Personagem
import RolandoAtributos
from Raca import escolher_raca

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
    
    
    personagem.set_raca(escolher_raca())

    print("\n=== Atributos finais do personagem ===")
    personagem.mostrarPersonagem()

if __name__ == "__main__":
    main()
