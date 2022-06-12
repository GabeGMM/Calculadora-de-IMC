print("Bem vindo a Calculadora de IMC")
#Olá esse é meu projeto de calculdora de IMC
while True: #enquanto for verdadeiro ele vai continuar rodando {    
    #pede o peso a altura da pessoa e depois printa[
    peso = input("Digite seu peso ex: 81.1: ")
    altura = int(input("Digite sua altura em CM: "))
    print(altura)
    #divide por 100 a altura
    altura = altura / 100
    print(altura)
#]
    #se o usuario digitar "," invés de "." ele tranforma em "."
    peso = float(peso.replace(',','.'))

    #faz o calculo do imc
    imc = (peso / (altura * altura))
    #faz o print dos resultados
    print(f'seu peso é: ', peso)
    print("sua altura é:", altura)
    print(f'O seu imc é: {imc:.2f}')
    #decide o IMC
    if (imc <= 18.5):
        print("Você está abaixo do peso")
    elif (imc >= 18.5) and (imc <= 24.9):
        print("Você está com o peso normal")
    elif (imc >= 25) and (imc <= 29.9):
        print("Você está com o peso normal")
    elif (imc >= 30):
        print("Você é obeso")
    #pergunta se quer continuar
    continuar = input("deseja calcular? s ou n")
    if continuar != 's' and continuar != 'S': #}
        break
print("******************************************************")
print(           "obrigado por usar a  calculadora")
print("******************************************************")
    

