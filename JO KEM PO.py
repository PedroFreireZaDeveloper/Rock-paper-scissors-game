import os
import random
R = "S"
while(R =="S"):
    print("Bem vindo ao jogo de Jo Ken Po\nPara jogar, digite as jogadas que o sistema irá pedir\nDigite '1' para simbolizar a jogada pedra\nDigite '2' para simbolizar a jogada papel\nDigite '3' para simbolizar a jogada tesoura\nVocê irá jogar contra o computador.\n")
    J1 = int(input("Digite a sua jogada:\n=======> "))
    J2 = random.randint (1,3)
    while J1 == 1 and J2 == 1 or J1 == 2 and J2 == 2 or J1 == 3 and J2 == 3:
        print("O jogo  empatou, digite a sua Jogada novamente.\n")
        J1 = int(input("Digite a sua jogada:\n======> "))
        J2 = random.randint (1,3)
    if J1 == 1 and J2 == 3 or J1 == 2 and J2 == 1 or J1 == 3 and J2 == 2:
        print("Você ganhou !!!")
    elif J2 == 1 and J1 == 3 or J2 == 2 and J1 == 1 or J2 == 3 and J1 == 2:
        print("O computador ganhou !!!\nVocê perdeu.")
    elif J1 >= 4 or J1 <= 0:
        print("\nVocê digitou um número inválido.")
    R = input("\nVocê quer jogar de novo ?\nDigite 'S' para sim ou 'N' para sair do programa.\n=======> ").upper()
    os.system('cls')