print('{:=^40}'.format(' LOJAS GUANABARA '))
valor = float(input('Valor do produto: R$'))
print('''FORMAS DE PAGAMENTO
 [1] À vista dinheiro/cheque
 [2] À vista cartão
 [3] 2x no cartão
 [4] 3x ou mais no cartão''')
op = int(input('Escolha um opção: '))
if op == 1:
     novo_valor = valor - (0.10 * valor)
     print('Valor com 10% de desconto será R${:.2f}'.format(novo_valor))
elif op == 2:
    novo_valor = valor - (0.05 * valor)
    print('Valor com 5% de desconto será R${:.2f}'.format(novo_valor))
elif op == 3:
    parcela = valor / 2
    print('O valor será de R${:.2f} parcelado em 2x de {:.2f}'.format(valor, parcela))
elif op == 4:
    novo_valor = valor + (0.20 * valor)
    valor_parc = int(input('Gostaria de parcelar em quantas vezes?'))
    if valor_parc >=3:
        parcela = novo_valor / valor_parc
        print('Valor a pagar com 20% de juros será R${:.2f} dividido em {} parcelas de R${:.2f}'.format(novo_valor, valor_parc, parcela))
    else:
        print('quantidade de parcela abaixo do permitido!')
else:
    print('OPÇÃO ERRADA!')







