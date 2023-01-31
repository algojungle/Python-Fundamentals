#!/usr/bin/env python
# coding : utf-8

'''
    Authentification
    Author : Joseph
    Date : 21.02.2023
'''

def main():
    '''authentification'''
    nombre = int(input('Entrez un nombre:'))

    if nombre != 0:
        inverse = 1.0 / nombre
        print(f'Inverse de {nombre} = {inverse}')

    if nombre != 0:
        inverse = 1.0 / nombre
        print(f'Inverse de {nombre} = {inverse}')
    else:
        print('Le nombre doit être différent de 0')

    if nombre > 0:
        inverse = 1.0 / nombre
        print(f'Inverse de {nombre} = {inverse}')
    elif nombre < 0:
        inverse = - 1.0 / nombre
        print(f'Inverse de {nombre} = {inverse}')
    else:
        print('Le nombre doit être différent de 0')

if __name__ == "__main__":
    main()
