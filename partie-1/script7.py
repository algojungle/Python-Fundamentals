#!/usr/bin/env python
# coding : utf-8

'''
    Table de multiplication
    Author : Joseph
    Date : 21.02.2023
'''

def main():
    '''table de multiplication'''
    nombre = int(input('Entrez un nombre:'))

    for cpt in range(10):
        print(f'{nombre} * {cpt+1} = {nombre * (cpt+1)}')

if __name__ == "__main__":
    main()
