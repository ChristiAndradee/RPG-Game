class Classe:
    def __init__(self, nome, habilidades):
        self.nome = nome
        self.habilidades = habilidades


class Bardo(Classe):
    def __init__(self):
        super().__init__(
            nome="Bardo",
            habilidades=["Inspiração", "Música Mágica", "Conhecimento Amplo"]
        )


class Paladino(Classe):
    def __init__(self):
        super().__init__(
            nome="Paladino",
            habilidades=["Imposição das Mãos", "Aura Sagrada", "Juramento"]
        )


class Ranger(Classe):
    def __init__(self):
        super().__init__(
            nome="Ranger",
            habilidades=["Companheiro Animal", "Explorador", "Arqueiria"]
        )


def escolher_classe():
    classes_disponiveis = {
        "1": Bardo,
        "2": Paladino,
        "3": Ranger
    }

    print("\n=== Escolha a Classe do Personagem ===")
    for k, v in classes_disponiveis.items():


        temp = v()
        print(f"{k} - {temp.nome}")

    while True:
        escolha = input("Digite o número da classe escolhida: ")
        if escolha in classes_disponiveis:
            instancia = classes_disponiveis[escolha]() 
            return instancia.nome 
        else:
            print("Opção inválida! Tente novamente.")