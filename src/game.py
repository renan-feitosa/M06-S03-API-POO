import time
from zoologico import Zoologico
from recinto import Recinto
from animal import Animal

zoo = Zoologico("My Zoo")

def jogar():

   
        # tela_inicio()
        # opcao = input("")
        # tutorial()
        while True:
            menu_geral()

def tela_inicio():
    print("                        ,-------.              ")
    print(" ,--,--,--.,--. ,--.    `--.   /  ,---.  ,---. ")
    print(" |        | \  '  /       /   /  | .-. || .-. |")
    print(" |  |  |  |  \   '       /   `--.' '-' '' '-' '")
    print(" `--`--`--'.-'  /       `-------' `---'  `---' ")
    print("           `---'                                ")

    print("(ღ˘⌣˘ღ) Bem-vindos ao My Zoo, o melhor zoológico virtual! Para jogar, pressione Enter")
    # print("1. Alimentar animais")
    # print("2. Limpar recintos")
    # print("3. Mostrar recintos")
    # print("4. Mostrar dinheiro")
    # print("5. Atrair visitantes")
    # print("0. Sair do jogo")

def tutorial():
    print("\nhm??")
    time.sleep(2)
    print('\n(╯°□°)╯ COMOOOO ASSIMMMM??????? Você não tem um zoológico ainda????')
    time.sleep(2)
    print('\nComo você quer jogar sem um zoológico, bobinho? Vamos criar um agora!')
    time.sleep(3)
    nome_zoo = input("\nQual vai ser o nome do seu zoológico?༼ つ ╹ ╹ ༽つ ")
    time.sleep(1)
    criar_zoo(nome_zoo)
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

def criar_zoo(nome):
    zoo = Zoologico(nome)

def menu_geral():
    print("\n")
    print('1. Ver zoológico')
    print("2. Mostrar recintos")
    print("3. Abrir para visitantes")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        menu_zoo()
    elif opcao == "2":
        menu_recintos()
    elif opcao == "3":
        abrir_zoo()
    else:
        print("Opção inválida")

def menu_zoo():
    print("\n")
    print(f'Nome: {zoo.nome()}')
    print(f'Dinheiro: {zoo.dinheiro()}')
    print(f'Número de recintos: {zoo.recintos_quantidade()}')
    print(f'Número de animais: {zoo.animais_quantidade()}')
    print("\n0. Voltar")

    opcao = input("Escolha uma opção: ")
    if opcao == "0":
        return
    else:
        print("Opção inválida")

def menu_recintos():

    print("\n")
    print("1. Adicionar recinto")
    print("2. Remover recinto")
    print('3. Ver animais sem recinto')  
    if zoo.recintos_quantidade() > 0:
        index = 4
        for recinto in zoo.mostrar_recintos():
            print(f"{index}. Ver {recinto}")
            index += 1
    else:
        print("Nenhum recinto a ser mostrado")
    print("\n0. Voltar")
    opcao = input("Escolha uma opção: ")
    index = 3
    if zoo.recintos_quantidade() == 0:
        pass
    if zoo.recintos_quantidade() == 1:
        if opcao == "3":
            animais_sem_recinto()
    if zoo.recintos_quantidade() > 1:
        for recinto in zoo.mostrar_recintos():
            if opcao == str(index):
                menu_recinto(recinto)
            index += 1
    if opcao == "1":
        criar_recinto()
    elif opcao == "2":
        remover_recinto()
    elif opcao == "3":
        animais_sem_recinto()
    elif opcao == "0":
        return
    else:
        print("Opção inválida")

def criar_recinto():
    especie = input("Qual a espécie dos animais desse recinto? ")
    recinto = Recinto(especie)
    zoo.adicionar_recinto(recinto)
    print(f"Recinto de {especie} criado com sucesso")

def remover_recinto():
    nome = input("Qual o nome do recinto a ser removido? ")
    for recinto in zoo.mostrar_recintos():
        if recinto == nome:
            zoo.remover_recinto(recinto)
    print(f"Recinto {nome} removido com sucesso")

def animais_sem_recinto():
    for animal in zoo.mostrar_animais():
        print(f"Nome: {animal[0]}")
        print(f"Espécie: {animal[1]}")
        print(f"Felicidade: {animal[2]}")

def menu_recinto(recinto):
    print("\n")
    print(f'Nome: {recinto.nome()}')
    print(f'Especie: {recinto.especie()}')
    print(f'Número de animais: {recinto.animais_quantidade()}')
    print(f'Limpeza: {recinto.limpeza()}')
    print("\n1. Adicionar animal")
    print("2. Remover animal")
    print("3. Alimentar animais")
    print("4. Limpar recinto")
    print("5. Sujar recinto")
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
    elif opcao == "5":
        sujar_recinto(recinto)
    elif opcao == "0":
        return
    else:
        print("Opção inválida")

if __name__ == "__main__":
    jogar()
