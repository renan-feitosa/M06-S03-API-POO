from recinto import Recinto
from animal import Animal

class Zoologico:
    def __init__(self, nome, recintos=[], ingresso=0, dinheiro=0):
        self.__nome = nome
        self.__recintos = recintos
        self.__ingresso = ingresso
        self.__dinheiro = dinheiro

    def nome(self):
        return self.__nome
    
    def adicionar_recinto(self, recinto):
        self.__recintos.append(recinto)
    
    def remover_recinto(self, recinto):
        if recinto in self.mostrar_recintos():
            self.__recintos.remove(recinto)
    
    def mostrar_recintos(self):
        recintos = []
        for recinto in self.__recintos:
            recintos.append(recinto.especie())

        return recintos
    
    def recintos_quantidade(self):
        return len(self.__recintos)
    
    def mostrar_animais(self):
        for recinto in self.__recintos:
            for animal in recinto.__animals:
                return animal.__name, animal.__species, animal.__happiness
    
    def animais_quantidade(self):
        quantidade = 0
        for recinto in self.__recintos:
            quantidade += len(recinto.__animals)
        return quantidade

    def dinheiro(self):
        return self.__dinheiro

    def preco_ingresso(self, valor):
        self.__ingresso = valor
    
    def atrair_visitantes(self):
        visitantes = 0
        for recinto in self.__recintos:
            if recinto.get_limpeza() > 7: 
                for animal in recinto.get_animais():
                    if animal.get_felicidade() > 8:
                        visitantes += 2
                    if animal.get_felicidade() > 5:
                        visitantes += 1
    
        self.__dinheiro += visitantes * self.__ingresso
        print(f"Zoológico atraiu {visitantes} visitantes, dinheiro atual: {self.__dinheiro}")