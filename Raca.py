class Raca:
    def __init__(self, nome, movimento, infravisao, alinhamento, habilidades):
        self.nome = nome
        self.movimento = movimento        
        self.infravisao = infravisao      
        self.alinhamento = alinhamento    
        self.habilidades = habilidades 

    def exibir_info(self):
        print(f"\n=== {self.nome.upper()} ===")
        print(f"Movimento: {self.movimento} metros")
        print(f"Infravisão: {self.infravisao if self.infravisao else 'Não'}")
        print(f"Alinhamento: {self.alinhamento}")
        print("Habilidades:")
        for hab in self.habilidades:
            print(f" - {hab}")


# ==== RAÇAS ESPECÍFICAS ====

class Humano(Raca):
    def __init__(self):
        super().__init__(
            nome="Humano",
            movimento=9,
            infravisao=False,
            alinhamento="Qualquer",
            habilidades=["Aprendizado", "Adaptabilidade"]
        )


class Anao(Raca):
    def __init__(self):
        super().__init__(
            nome="Anão",
            movimento=6,
            infravisao=18,
            alinhamento="Ordem",
            habilidades=["Mineradores", "Vigoroso", "Armas Grandes", "Inimigos"]
        )


class Gnomo(Raca):
    def __init__(self):
        super().__init__(
            nome="Gnomo",
            movimento=6,
            infravisao=18,
            alinhamento="Neutro",
            habilidades=["Avaliadores", "Sagazes e Vigorosos", "Restrições"]
        )


class Elfo(Raca):
    def __init__(self):
        super().__init__(
            nome="Elfo",
            movimento=9,
            infravisao=18,
            alinhamento="Neutro",
            habilidades=["Percepção Natural", "Graciosos", "Treinamento Racial", "Imunidades"]
        )


class Halfling(Raca):
    def __init__(self):
        super().__init__(
            nome="Halfling",
            movimento=6,
            infravisao=False,
            alinhamento="Neutro",
            habilidades=["Furtivo", "Destemido", "Bons de Mira", "Pequenos", "Restrições"]
        )


class MeioElfo(Raca):
    def __init__(self):
        super().__init__(
            nome="Meio-Elfo",
            movimento=9,
            infravisao=9,
            alinhamento="Caos",
            habilidades=["Aprendizado", "Graciosos e Vigorosos", "Idioma Extra", "Imunidades"]
        )

def escolher_raca():
    racas_disponiveis = {
        "1": Humano,
        "2": Anao,
        "3": Gnomo,
        "4": Elfo,
        "5": Halfling,
        "6": MeioElfo
    }

    print("\n=== Escolha a Raça do Personagem ===")
    for k, v in racas_disponiveis.items():
        rac = v()
        print(f"{k} - {rac.nome}")

    while True:
        escolha = input("Digite o número da raça escolhida: ")
        if escolha in racas_disponiveis:
            return racas_disponiveis[escolha]()
        else:
            print("Opção inválida! Tente novamente.")







