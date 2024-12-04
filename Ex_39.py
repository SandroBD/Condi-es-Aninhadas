from datetime import date
atual = date.today().year
nasc = int(input('Informe o ano de nascimento: '))
sex = str(input('Informe seu sexo:')).strip().title()
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18 and sex == 'Masculino':
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18 and sex == 'Masculino':
    print('Ainda faltam {} anos para o alistamento.'.format( 18 - idade))
    print('Seu alistamento será em {}'.format(nasc + 18))
elif idade > 18 and sex == 'Masculino':
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(nasc + 18))
else:
    print('O seu alistamento não é obrigatório.')





