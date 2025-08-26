#Criacao de personagem

class Personagem:

    def __init__(self, nome):
        self.__raca = ""
        self.__classe = ""
        self.__nome = nome
        self.__forca = 0
        self.__destreza = 0
        self.__constituicao = 0
        self.__inteligencia = 0
        self.__sabedoria = 0
        self.__carisma = 0
        self.__habilidades = ""

    #Getters

    def get_nome(self):
        return self.__nome

    def get_forca(self):
        return self.__forca
    
    def get_destreza(self):
        return self.__destreza
    
    def get_constituicao(self):
        return self.__constituicao
    
    def get_inteligencia(self):
        return self.__inteligencia
    
    def get_sabedoria(self):
        return self.__sabedoria
    
    def get_carisma(self):
        return self.__carisma
    
    def get_raca(self):
        return self.__raca
    
    def get_classe(self):
        return self.__classe
    
    def get_habilidades(self):
        return self.__habilidades
    
    #Setters
    
    def set_nome(self, def_nome):
         self.__nome = def_nome
    
    def set_forca(self, def_forca):
         self.__forca = def_forca
    
    def set_destreza(self, def_destreza):
         self.__destreza = def_destreza
    
    def set_constituicao(self, def_constituicao):
         self.__constituicao = def_constituicao
    
    def set_inteligencia(self, def_inteligencia):
         self.__inteligencia = def_inteligencia
    
    def set_sabedoria(self, def_sabedoria):
         self.__sabedoria = def_sabedoria
    
    def set_carisma(self, def_carisma):
         self.__carisma = def_carisma

    def set_raca(self, def_raca):
         self.__raca = def_raca

    def set_classe(self, def_classe):
         self.__classe = def_classe

    def set_habilidades(self, def_habilidades):
         self.__habilidades = def_habilidades

    def atribuir(self, atributos):
         self.__forca = atributos["Força"]
         self.__destreza = atributos["Destreza"]
         self.__constituicao = atributos["Constituição"]
         self.__inteligencia = atributos["Inteligência"]
         self.__sabedoria = atributos["Sabedoria"]
         self.__carisma = atributos["Carisma"]

    def mostrarPersonagem(self):
        print(f"\nNome: {self.get_nome()}")
        print(f"\nRaca: {self.get_raca()}")
        print(f"Classe: {self.get_classe()}")
        print(f"\nForça: {self.get_forca()}")
        print(f"Destreza: {self.get_destreza()}")
        print(f"Constituição: {self.get_constituicao()}")
        print(f"Inteligência: {self.get_inteligencia()}")
        print(f"Sabedoria: {self.get_sabedoria()}")
        print(f"Carisma: {self.get_carisma()}")
        print(f"\nHabilidades: {self.get_habilidades()}\n")

