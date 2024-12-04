print('Verificar se as retas formam um triângulo')
l1 = float(input('Informe o primeiro seguimento: '))
l2 = float(input('Informe o segundo seguimento: '))
l3 = float(input('Informe o terceiro seguimento: '))
if l1 + l2 > l3 and l2 +l3 > l1 and l3 + l1 > l2:
    print('Os seguimentos podem formar um triângulo ', end='')
    if l1 == l2 == l3:
        print('equilátero')
    elif l1 != l2 != l3 != l1:
        print('escaleno!')
    else:
        print('isósceles!')
else:
    print('Os seguimentos NÃO formam um triângulo')
