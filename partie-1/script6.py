#!/usr/bin/env python
# coding : utf-8

'''
    Table de multiplication
    Author : Joseph
    Date : 21.02.2023
'''

def main():
    '''authentification'''
    nombre = int(input('Entrez un nombre:'))

    cpt = 1
    while cpt <= 10:
        print(f'{nombre} * {cpt} = {nombre * cpt}')
        cpt += 1
        # cpt = cpt + 1

if __name__ == "__main__":
    main()
