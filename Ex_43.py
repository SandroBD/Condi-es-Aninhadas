kg = float(input('Informe seu peso (Kg): '))
altura = float(input('Informe sua altura: '))
IMC = kg / (altura ** 2)
print('IMC= {:.2f}'.format(IMC,))
if IMC < 18.5:
    print('Abaixo do peso!')
elif 18.5 <= IMC < 25:
    print('Peso ideal!')
elif 25 <= IMC < 30:
    print('Sobrepeso!')
elif 30 <= IMC < 40:
    print('Obesidade!')
else:
    print('Obesidade Mórbida!')





