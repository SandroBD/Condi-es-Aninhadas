numero = int(input('Informe um número inteiro: '))
print('Informe a base de conversão: \n[1] para binário\n[2] para octal\n[3] para hexadecimal')
base = int(input('Sua opção: '))
if base == 1:
    binario = bin(numero)[2:]
    print('O número {} em binário é {}'.format(numero,binario))
elif base == 2:
    octal = oct(numero)[2:]
    print('O número {} em octal é {}'.format(numero,octal))
elif base == 3:
    hexa = hex(numero)[2:]
    print('O número {} em hexadecimal é {}'.format(numero,hexa))
else:
    print('Opção Errada')




