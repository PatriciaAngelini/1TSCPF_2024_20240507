titulo = 'Estado onde nasceu'
print(f'{titulo:^30}')

estado = input('Entre o estado onde nasceu: ').upper()

if estado in ('SP', 'SAO PAULO', 'SÃO PAULO'):
    print('Paulista')
elif estado == 'RJ':
    print('Carioca')
else:
    print('Outros Estados')
