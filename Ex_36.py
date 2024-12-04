print('{}EMPRESTIMO{}'.format('='*4,'='*4))
valor = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe seu salário: R$'))
ano = int(input('Parcelar em quantos anos? '))
prestacao = valor / ( ano * 12)
minimo = salario * 0.3
if prestacao > 0.3 * salario:
    print('O valor da prestação de {} excede o valor mínimo de {}! \nEmprestimo negado!'.format(prestacao, minimo))
else:
    print('Emprestimo aprovado \nparcelado em {} anos no valor de R$ {:.2f}'.format(ano,prestacao))


