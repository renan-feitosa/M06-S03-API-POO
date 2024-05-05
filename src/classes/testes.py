import pytest
from zoologico import Zoologico
from recinto import Recinto
from animal import Animal


# Testar a API do animal
def test_animal_nome():
    animal = Animal("Leão", "Leão")
    assert animal.nome() == "Leão"

def test_animal_especie():
    animal = Animal("Leão", "Leão")
    assert animal.especie() == "Leão"

def test_animal_comer():
    animal = Animal("Leão", "Leão")
    animal.comer()
    assert animal.felicidade() == 1

def test_animal_get_felicidade():
    animal = Animal("Leão", "Leão")
    assert animal.get_felicidade() == 0

def test_animal_perder_felicidade():
    animal = Animal("Leão", "Leão")
    animal.comer()
    animal.perder_felicidade()
    assert animal.felicidade() == 0

    animal.perder_felicidade()
    assert animal.felicidade() == 0




# Testar a API do recinto
def test_recinto_especie():
    recinto = Recinto("Leão")
    assert recinto.especie() == "Leão"

def test_recinto_alterar_especie():
    recinto = Recinto("Leão")
    recinto.alterar_especie("Felinos")
    assert recinto.especie() == "Felinos"


def test_recinto_adicionar_animal():
    recinto = Recinto("Felino")
    animal = Animal("Leão", "Felino")
    recinto.adicionar_animal(animal)
    assert animal in recinto.mostrar_animais()

def test_recinto_remover_animal():
    recinto = Recinto("Leão")
    animal = Animal("Leão", "Leão")
    recinto.adicionar_animal(animal)
    recinto.remover_animal(animal)
    assert animal not in recinto.mostrar_animais()

def test_recinto_mostrar_animais():
    recinto = Recinto("Leão")
    animal = Animal("Leão", "Leão")
    recinto.adicionar_animal(animal)
    assert animal in recinto.mostrar_animais()

def test_recinto_animais_quantidade():
    recinto = Recinto("Girafa")

    animal = Animal("Melwin", "Girafa")
    recinto.adicionar_animal(animal)
    assert recinto.animais_quantidade() == 1

    animal2 = Animal("Girafa aleatória", "Girafa")
    recinto.adicionar_animal(animal2)
    assert recinto.animais_quantidade() == 2

def test_recinto_alimentar_recinto():
    recinto = Recinto("Leão")
    animal = Animal("Leão", "Leão")
    recinto.adicionar_animal(animal)
    recinto.alimentar_recinto()
    assert animal.felicidade() == 1

def test_recinto_limpeza():
    recinto = Recinto("Leão")
    recinto.limpar_recinto()
    assert recinto.limpeza() == 10

def test_recinto_sujar_recinto():
    recinto = Recinto("Leão")
    recinto.sujar_recinto() # 4
    recinto.sujar_recinto() # 3
    recinto.sujar_recinto() # 2
    recinto.sujar_recinto() # 1
    assert recinto.limpeza() == 1

    recinto.sujar_recinto() # 0
    assert recinto.limpeza() == 0

    recinto.sujar_recinto() # 0
    assert recinto.limpeza() == 0





# Testar a API do zoológico
def test_zoo_nome():
    zoo = Zoologico("Zoo")
    assert zoo.nome() == "Zoo"

def test_zoo_adicionar_recinto():
    zoo = Zoologico("Zoo")
    recinto = Recinto("Leão")
    zoo.adicionar_recinto(recinto)
    assert recinto in zoo.mostrar_recintos()

def test_zoo_remover_recinto():
    zoo = Zoologico("Zoo")
    recinto = Recinto("Leão")
    zoo.adicionar_recinto(recinto)
    zoo.remover_recinto(recinto)
    assert recinto not in zoo.mostrar_recintos()

def test_zoo_mostrar_recintos():
    zoo = Zoologico("Zoo")
    recinto = Recinto("Leão")
    zoo.adicionar_recinto(recinto)
    assert recinto in zoo.mostrar_recintos()

def test_zoo_recintos_quantidade():
    zoo = Zoologico("Zoo")
    recinto = Recinto("Leão")
    zoo.adicionar_recinto(recinto)
    assert zoo.recintos_quantidade() == 1

def test_zoo_mostrar_animais():
    zoo = Zoologico("Zoo")
    recinto = Recinto("Leão")
    animal = Animal("Simba", "Leão")
    animal2 = Animal("Nala", "Leão")
    
    recinto.adicionar_animal(animal)
    recinto.adicionar_animal(animal2)
    zoo.adicionar_recinto(recinto)

    assert animal in zoo.mostrar_animais()
    assert animal2 in zoo.mostrar_animais()

def test_zoo_animais_quantidade():
    zoo = Zoologico("Zoo")
    recinto = Recinto("Leão")
    animal = Animal("Leão", "Leão")
    recinto.adicionar_animal(animal)
    zoo.adicionar_recinto(recinto)
    assert zoo.animais_quantidade() == 1





# Executar os testes
if __name__ == "__main__":
    pytest.main(["-v", "--tb=native", __file__])