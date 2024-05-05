class Animal:
    def __init__(self, nome, especie, felicidade=0):
        self.__nome = nome
        self.__species = especie
        self.__happiness = felicidade

    def nome(self):
        return self.__nome
    
    def comer(self):
        self.__happiness += 1
        print(f"{self.__name} está satisfeito, felicidade atual: {self.__happiness}")

    def get_felicidade(self):
        return self.__happiness
    
    def perder_felicidade(self):
        if self.__happiness > 0:
            self.__happiness -= 1
            print(f"{self.__name} perdeu felicidade, felicidade atual: {self.__happiness}")