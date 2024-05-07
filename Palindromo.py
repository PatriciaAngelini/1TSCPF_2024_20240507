# palavra1 = 'Giovanna'
# palavra2 = 'chegou'
#
# frase = palavra1 + ' ' + palavra2
# print(frase)
#
# fraseinversa = palavra2 + ' ' + palavra1
# print(fraseinversa)
titulo = 'Palindromo'
#teste REVIVER, ANTONIO
print(f'{titulo:^30}')
resp = 's'
while resp in ('s','sim', 'y', 'yes', 'sí'):
    palavra = input('Entre com a palavra: ')
    reversa = ''
    for letra in palavra:
        reversa = letra + reversa
    if palavra == reversa:
        print(f'A palavra {palavra} é palidromo')
    else:
        print(f'A palavra {palavra} não é palidromo')
    resp = input('Quer continuar a brincar? ').lower()


