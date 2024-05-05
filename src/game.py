import time
from classes.zoologico import Zoologico
from classes.recinto import Recinto
from classes.animal import Animal
from api import criar_zoo, abrir_zoo, get_zoo_info, get_recintos_info, create_recinto, delete_recinto, get_recinto_info, create_animal, delete_animal, post_alimentar_animais, post_limpar_recinto



def jogar():
        tela_inicio()
        opcao = input("")
        zoo = tutorial()
        while True:
            menu_geral(zoo)

# TUTORIAL ---------------------------------------------------------------------------------------

def tela_inicio():
    print("                        ,-------.              ")
    print(" ,--,--,--.,--. ,--.    `--.   /  ,---.  ,---. ")
    print(" |        | \  '  /       /   /  | .-. || .-. |")
    print(" |  |  |  |  \   '       /   `--.' '-' '' '-' '")
    print(" `--`--`--'.-'  /       `-------' `---'  `---' ")
    print("           `---'                                ")

    print("(ღ˘⌣˘ღ) Bem-vindos ao My Zoo, o melhor zoológico virtual! Para jogar, pressione Enter")

def tutorial():
    print("\nhm??")
    time.sleep(2)
    print('\n(╯°□°)╯ COMOOOO ASSIMMMM??????? Você não tem um zoológico ainda????')
    time.sleep(2)
    print('\nComo você quer jogar sem um zoológico, bobinho? Vamos criar um agora!')
    time.sleep(3)
    nome_zoo = input("\nQual vai ser o nome do seu zoológico?༼ つ ╹ ╹ ༽つ ")
    time.sleep(1)

    zoo = criar_zoo(nome_zoo)

    print(f"\nLegaal! ٩(^‿^)۶ O {nome_zoo} agora existe!")
    time.sleep(2)
    print("\n.")
    time.sleep(2)
    print("..")
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("Tá meio vazio, né? (•‿•)")
    time.sleep(2)
    print("\nSei lá, acho que você devia adicionar um recinto e depois adicionar animais nele ou algo assim...")
    time.sleep(2)
    print("Vou deixar você explorar por conta própria! (⊙_⊙)")
    return zoo


# MENU INICIAL ---------------------------------------------------------------------------------------

def menu_geral(zoo):
    print("\n")
    print('1. Ver zoológico')
    print("2. Mostrar recintos")
    print("3. Abrir para visitantes")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        menu_zoo(zoo)
    elif opcao == "2":
        menu_recintos(zoo)
    elif opcao == "3":
        abrir_zoo(zoo)
    else:
        print("Opção inválida")



# MENU FICHA ZOOLÓGICO ---------------------------------------------------------------------------------------

def menu_zoo(zoo):
    data = get_zoo_info(zoo)

    print("\n")
    print("----------------------------------------------------")
    print(f'Nome: {data[0]}')
    print(f'Dinheiro: {data[1]}')
    print(f'Número de recintos: {data[2]}')
    print(f'Número de animais: {data[3]}')
    print("----------------------------------------------------")
    time.sleep(1.5)
    print("\n0. Voltar")

    opcao = input("Escolha uma opção: ")
    if opcao == "0":
        return
    else:
        print("Opção inválida")
        menu_zoo(zoo)



# MENU RECINTOS ---------------------------------------------------------------------------------------

def menu_recintos(zoo):
    data = get_recintos_info(zoo)

    print("\n")
    print("1. Adicionar recinto")
    print("2. Remover recinto")
    index = 3
    for recinto in data:
        print(f"{index}. Ver {recinto.especie()}")
        index += 1
    print("\n0. Voltar")
    opcao = input("Escolha uma opção: ")
    index = 3
    for recinto in data:
        if opcao == str(index):
            menu_lista_recintos(recinto)
        index += 1
    if opcao == "1":
        criar_recinto(zoo)
    elif opcao == "2":
        remover_recinto(zoo)
    elif opcao == "0":
        return
    else:
        print("Opção inválida")
        menu_recintos(zoo)



# Criar, remover e listar recintos ---------------------------------------------------------------------------------------
def criar_recinto(zoo):
    especie = input("Qual a espécie dos animais desse recinto? ")
    recinto = create_recinto(zoo, especie)
    print(f"Recinto de {recinto.especie()} criado com sucesso")
    time.sleep(1.5)
    menu_recintos(zoo) 

def remover_recinto(zoo):
    nome = input("Qual o nome do recinto a ser removido? ")
    data = get_recintos_info(zoo)
    for recinto in data:
        if recinto.especie() == nome:
            delete_recinto(zoo, recinto)
            print(f"Recinto de {nome} removido com sucesso")
            time.sleep(1.5)
        else:
            print("Recinto não encontrado")
            time.sleep(1.5)
    menu_recintos(zoo)

def menu_lista_recintos(recinto):
    data = get_recinto_info(recinto)
    print("\n")
    print("----------------------------------------------------")
    print(f'Nome: Recinto de {data[0]}')
    print(f'Número de animais: {data[1]}')
    print(f'Limpeza: {data[2]}')
    print("----------------------------------------------------")
    print("Animais:")
    for animal in data[3]:
        print(f"Nome: {animal.nome()} Felicidade: {animal.felicidade()}")
    print('----------------------------------------------------')
    time.sleep(1.5)
    print("\n1. Adicionar animal")
    print("2. Remover animal")
    print("3. Alimentar animais")
    print("4. Limpar recinto")
    print("0. Voltar")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionar_animal(recinto)
    elif opcao == "2":
        remover_animal(recinto)
    elif opcao == "3":
        alimentar_animais(recinto)
    elif opcao == "4":
        limpar_recinto(recinto)
    elif opcao == "0":
        return
    else:
        print("Opção inválida")
        menu_lista_recintos(recinto)



#  Adicionar, remover, alimentar e limpar animais ---------------------------------------------------------------------------------------
def adicionar_animal(recinto):
    nome = input("Qual vai ser o nome do seu novo animal? ")
    especie = recinto.especie()
    animal = create_animal(recinto, nome, especie)
    print(f"{animal.nome()} adicionado ao Recinto de {recinto.especie()} com sucesso")
    time.sleep(1.5)
    menu_lista_recintos(recinto)

def remover_animal(recinto):
    nome = input("Qual o nome do animal a ser removido? ")
    data = get_recinto_info(recinto)
    for animal in data[3]:
        if animal.nome() == nome:
            delete_animal(recinto, animal)
            print(f"{nome} removido com sucesso")
            time.sleep(1.5)
    menu_lista_recintos(recinto)

def alimentar_animais(recinto):
    post_alimentar_animais(recinto)
    print("Animais alimentados com sucesso")
    time.sleep(1.5)
    menu_lista_recintos(recinto)

def limpar_recinto(recinto):
    post_limpar_recinto(recinto)
    print("Recinto limpo com sucesso")
    time.sleep(1.5)
    menu_lista_recintos(recinto)

# Iniciar jogo -----------------------------------------------------------------------------------
if __name__ == "__main__":
    jogar()
