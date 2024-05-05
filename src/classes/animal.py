class Animal:
    def __init__(self, nome, especie, felicidade=5):
        self.__nome = nome
        self.__especie = especie
        self.__felicidade = felicidade

    def nome(self):
        return self.__nome
    
    def especie(self):
        return self.__especie
    
    def felicidade(self):
        return self.__felicidade
    
    def comer(self):
        if self.__felicidade < 10:
            self.__felicidade += 1
    
    def perder_felicidade(self):
        if self.__felicidade > 0:
            self.__felicidade -= 1