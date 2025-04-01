#numeros escolhidos pelo usuario
num1= input("Digite o primeiro numero: ")
num2= input("Digite o segundo numero: ")
#convertendo os numeors
num1=float(num1)
num2=float(num2)
#selecionar a operação
opc=input("selecione a operação onde soma é 0, subitracao é 1, divisao é 2, multiplica é 3: ")
opc= int(opc)
#lista de operações
list_oprecao = ['soma','subitracao', 'divisao', 'multipocacao']

if 'soma' in list_oprecao[opc]:
    print(num1+num2)
elif 'subitracao' in list_oprecao[opc]:
    print(num1-num2)
elif 'divisao' in list_oprecao[opc]:
      print(num1/num2)
elif 'multipocacao' in list_oprecao[opc]:
        print(num1*num2)