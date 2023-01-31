#!/usr/bin/env python
# coding : utf-8

'''
    Gestion des erreurs
    Author : Joseph
    Date : 28.02.2023
'''

def main():
    '''try..except..else..finally'''
    nombre = int(input('Entrez un nombre:'))
    
    # inverse = 1.0 / nombre
    # print(f'Inverse de {nombre} = {inverse}')
    
    # try:
    #     inverse = 1.0 / nombre
    #     print(f'Inverse de {nombre} = {inverse}')
    # except ZeroDivisionError as e:
    #     print(e)
    #     print('Le nombre doit être différent de 0')
    # except TypeError as e:
    #     # print("L'entrée est invalide")
    #     inverse = 1.0 / int(nombre)
    #     print(f'Inverse de {nombre} = {inverse}')

    try:
        # assert nombre >= 0
        if nombre < 0:
            raise Exception('ceci est une erreur personnalisée')
        inverse = 1.0 / nombre
        print(f'Inverse de {nombre} = {inverse}')
    except AssertionError as e:
        print(e)
        print('Le nombre doit être supérieur à 0')
    except Exception as e:
        print(e)
        print('Le nombre doit être différent de 0')
    else:
        print("L'invsere a été bien calculé")
    finally:
        print("Ceci s'exécute toujours")

if __name__ == "__main__":
    main()
