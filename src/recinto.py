from animal import Animal

class Recinto:
    def __init__(self, especie, animais=[], limpeza=5):
        self.__especie = especie
        self.__animals = animais
        self.__limpeza = limpeza

    def nome(self):
        return self.__nome
    
    def especie(self):
        return self.__especie

    def animais_quantidade(self):
        return len(self.__animals)
    
    def mostrar_animais(self):
        for animal in self.__animals:
            return animal.__name, animal.__species, animal.__happiness
    
    def limpeza(self):
        return self.__limpeza
    
    def adicionar_animal(self, animal):
        if animal.__species == self.__especie:
            self.__animals.append(animal)
        else:
            raise ValueError("Animal não é da mesma espécie do recinto")
    
    def remover_animal(self, animal):
        if animal in self.__animals:
            self.__animals.remove(animal)
        else:
            raise ValueError("Animal não está no recinto")
    
    def alterar_nome(self, nome):
        self.__nome = nome

    def alimentar_recinto(self):
        for animal in self.__animals:
            animal.comer()
    
    def limpar_recinto(self):
        self.__limpeza = 10
        print(f"Recinto {self.__nome} limpo")
    
    def sujar_recinto(self):
        self.__limpeza -= 1
        print(f"Recinto {self.__nome} está ficando sujo, limpeza atual: {self.__limpeza}")