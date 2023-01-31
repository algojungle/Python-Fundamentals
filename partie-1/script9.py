#!/usr/bin/env python
# coding : utf-8

'''
    Structures de données : Les dictionnaires
    Author : Joseph
    Date : 21.02.2023
'''

from pprint import pprint

def main():
    # Création d'une dictionnaire
    personne = {
        'nom': 'John',
        'age': 18,
        'sexe': 'M',
        'profession': 'Développeur',
        'adresse': 'Lomé, Rue de la joie, 42',
        'skills': ['Python', 'Excel', 'HTML']
    }
    # Afficher le dictionnaire
    pprint(personne)
    # Afficher un élément
    print(personne['nom'])
    # Modifier un élément
    personne['age'] = 26
    # La liste des clés
    pprint(list(personne.keys()))
    # La liste des valeurs
    pprint(list(personne.values()))

if __name__ == "__main__":
    main()
