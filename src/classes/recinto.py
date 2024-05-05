from classes.animal import Animal

class Recinto:
    def __init__(self, especie, animais=None, limpeza=5):
        self.__especie = especie
        self.__animais = animais if animais is not None else []
        self.__limpeza = limpeza
    
    def especie(self):
        return self.__especie

    def animais_quantidade(self):
        return len(self.__animais)
    
    def mostrar_animais(self):
        animais = []
        for animal in self.__animais:
            animais.append(animal)
        
        return animais
    
    def limpeza(self):
        return self.__limpeza
    
    def adicionar_animal(self, animal):
        self.__animais.append(animal)

    
    def remover_animal(self, animal):
        if animal in self.__animais:
            self.__animais.remove(animal)
        else:
            raise ValueError("Animal não está no recinto")
    
    def alterar_especie(self, especie):
        self.__especie = especie

    def alimentar_recinto(self):
        for animal in self.__animais:
            animal.comer()
    
    def limpar_recinto(self):
        self.__limpeza = 10
    
    def sujar_recinto(self):
        if self.__limpeza > 0:
            self.__limpeza -= 1