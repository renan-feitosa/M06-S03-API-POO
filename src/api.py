from classes.zoologico import Zoologico
from classes.recinto import Recinto
from classes.animal import Animal

def criar_zoo(nome):
    zoo = Zoologico(nome)
    return zoo

def abrir_zoo(zoo):
    zoo.abrir_zoo()

def get_zoo_info(zoo):
    return zoo.nome(), zoo.dinheiro(), zoo.recintos_quantidade(), zoo.animais_quantidade()

def get_recintos_info(zoo):
    recintos = []
    for recinto in zoo.mostrar_recintos():
        recintos.append(recinto)
    return recintos

def create_recinto(zoo, especie):
    recinto = Recinto(especie)
    zoo.adicionar_recinto(recinto)
    return recinto

def delete_recinto(zoo, recinto):
    zoo.remover_recinto(recinto)
    return

def get_recinto_info(recinto):
    return recinto.especie(), recinto.animais_quantidade(), recinto.limpeza(), recinto.mostrar_animais()

def create_animal(recinto, nome, especie):
    animal = Animal(nome, especie)
    recinto.adicionar_animal(animal)
    return animal

def delete_animal(recinto, animal):
    recinto.remover_animal(animal)
    return

def post_alimentar_animais(recinto):
    recinto.alimentar_recinto()
    return

def post_limpar_recinto(recinto):
    recinto.limpar_recinto()
    return