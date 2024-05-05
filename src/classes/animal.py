class Animal:
    def __init__(self, nome, especie, felicidade=0):
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
        self.__felicidade += 1
        print(f"{self.__nome} está satisfeito, felicidade atual: {self.__felicidade}")

    def get_felicidade(self):
        return self.__felicidade
    
    def perder_felicidade(self):
        if self.__felicidade > 0:
            self.__felicidade -= 1
            print(f"{self.__nome} perdeu felicidade, felicidade atual: {self.__felicidade}")