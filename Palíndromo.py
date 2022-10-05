#ENUNCIADO:
#Crie um programa que leia uma frase ou palavra (desconsiderando
#os espaços) e no fim diga se ali existe ou não um palíndromo.
#Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA,
#O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA
novamente = "S"
while novamente == 'S':
    frase = str(input("Qual frase a ser lida?")).strip().upper()
    blocks = frase.split()
    juntando = "".join(blocks)
    inverso = juntando[::-1]
    print(f"\nA frase original (sem espaços) é: {juntando}\n\nE a frase lida ao contrário fica assim -> {inverso}")
    if juntando == inverso:
        print("\n====Temos um palíndromo!====")
    else:
        print("\n====Não temos um palíndromo!====")
    novamente = str(input("\nQuer testar outra palavra ou frase?\nSE QUISER -> Digite [S] para Sim (CONTINUAR O PROGRAMA)\nSE NÃO QUISER ->Pressione qualquer tecla para finalizar esse programa.").strip().upper())
print("Obrigado!Até a próxima vez!")






