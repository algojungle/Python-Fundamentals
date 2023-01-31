#!/usr/bin/env python
# coding : utf-8

'''
    Écrire un programme Python qui effectue les actions suivantes
    1. Saisir les noms de n étudiants
    2. Afficher la liste des étudiants
    3. Saisir les notes des étudiants (3 matières)
    4. Calcule les moyennes des étudiants
    5. Calcule le rang des étudiants suivant les moyennes
    6. Sauvegarder les notes des étudiants dans un fichier
    7. Afficher la liste des étudiants avec leurs notes depuis le fichier.
'''

# Modules
from pprint import pprint

from module import *


# Constantes
FILENAME = 'base_etudiants.json'


def main():
    # 0. Saisie la taille de l'effectif
    n = int(input('Total students: '))

    # 1. Saisir les noms de n étudiants
    etudiants = saisir_liste_etudiants(n)

    # 2. Afficher la liste des étudiants
    afficher_effectif(etudiants)

    # 3. Saisir les notes des étudiants (3 matières)
    notes = saisir_notes(etudiants)

    # 4. Calcule les moyennes des étudiants
    moyennes = calculer_moyenne(notes)

    # 5. Calcule le rang des étudiants suivant les moyennes
    rang = calcul_rang(moyennes)

    # 6. Sauvegarder les notes des étudiants dans un fichier
    exporter_etudiant(etudiants, notes, moyennes, rang, FILENAME)

    # 7. Afficher la liste des étudiants avec leurs notes depuis le fichier.
    base_etudiants = charger_etudiant(FILENAME)
    pprint(base_etudiants)


if __name__ == '__main__':
    main()
