from classes.recinto import Recinto

class Zoologico:
    def __init__(self, nome, recintos=None, ingresso=100, dinheiro=0):
        self.__nome = nome
        self.__recintos = recintos if recintos is not None else []
        self.__ingresso = ingresso
        self.__dinheiro = dinheiro

    def nome(self):
        return self.__nome
    
    def adicionar_recinto(self, recinto):
        if not isinstance(recinto, Recinto):
            raise ValueError("Não é um recinto")
        
        self.__recintos.append(recinto)


    def remover_recinto(self, recinto):
        if recinto in self.mostrar_recintos():
            self.__recintos.remove(recinto)
    
    def mostrar_recintos(self):
        recintos = []
        for recinto in self.__recintos:
            recintos.append(recinto)

        return recintos
    
    def recintos_quantidade(self):
        return len(self.__recintos)
    
    def mostrar_animais(self):
        animais = []
        for recinto in self.__recintos:
            for animal in recinto.mostrar_animais():
                animais.append(animal)
        
        return animais
    
    def animais_quantidade(self):
        quantidade = 0
        for recinto in self.__recintos:
            quantidade += recinto.animais_quantidade()
        return quantidade

    def dinheiro(self):
        return self.__dinheiro
    
    def abrir_zoo(self):
        visitantes = 0
        for recinto in self.__recintos:
            if recinto.limpeza() > 6: 
                for animal in recinto.mostrar_animais():
                    if animal.felicidade() > 8:
                        visitantes += 2
                    if animal.felicidade() > 5:
                        visitantes += 1
    
        self.__dinheiro += visitantes * 50
        print(f"Zoológico atraiu {visitantes} visitantes, dinheiro atual: {self.__dinheiro}")