#QUEBRADO!

p = int(input('Qual é o número de pessoas? '))
i = int(input('Qual é a idade dos usuários? '))


if p == 1:
    print('Bem triste ver filme sozinho!')
elif input('Qual é número de pessoas? '):
    
    
    if i < 3:
        print('Ingresso gratuito!')
    if i == 3 or i <= 12:
        print('O ingresso entre 3 e 12 anos custa R$15!')
    if i > 12:
        print('O ingresso acima dos 12 anos custa R$30!')
    