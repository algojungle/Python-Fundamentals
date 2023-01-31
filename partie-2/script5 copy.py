#!/usr/bin/env python
# coding : utf-8

'''
    Gestion des erreurs
    Author : Joseph
    Date : 28.02.2023
'''

from getpass import getpass

def main():
    '''try..except..else..finally'''
    # password = getpass('Entrez votre mot de passe:')
    password = input('Entrez votre mot de passe:')
    
    try:
        if len(password) < 8:
            raise Exception('le mot de passe est trop court')
        if password.upper() == password:
            raise Exception('le mot doit contenir au moins une minuscule')
        if password.lower() == password:
            raise Exception('le mot doit contenir au moins une majuscule')
    except Exception as e:
        print(e)
    else:
        print("Le mot de passe est valide")
    finally:
        print("Ceci s'exécute toujours")

if __name__ == "__main__":
    main()
