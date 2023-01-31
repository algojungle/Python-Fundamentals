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


import os


N_MATIERES = 3
FILE = 'base_etudiants.txt'


def saisir_etudiants(nb_etudiants):
    liste_etudiants = []
    for i in range(nb_etudiants):
        etudiant = input(f"Nom de l'étuidant n°{i+1} : ").strip()
        liste_etudiants.append(etudiant)

    return liste_etudiants


def affichier_etudiants(liste_etudiants):
    print('*** Liste des étudiants ***')
    for i, etudiant in enumerate(liste_etudiants):
        print(i, etudiant)


def saisir_notes(liste_etudiants):
    notes = []
    for i, etudiant in enumerate(liste_etudiants):
        print(f"Nom de l'étuidant n°{i+1} : {etudiant}")
        notes_etudiant = []
        for j in range(N_MATIERES):
            note = int(input(f'Note de la matière {j+1} : '))
            notes_etudiant.append(note)
        notes.append(notes_etudiant)

    return notes

def calcule_moyenne(notes):
    moyennes = []
    for i in range(len(notes)):
        moyenne = 0
        for j in range(N_MATIERES):
            moyenne += notes[i][j]

        moyenne = moyenne / N_MATIERES
        moyennes.append(moyenne)

    return moyennes

def main():
    '''main function prints hello world'''
    # 0. Saisie du nombre d'étudiants
    n = int(input("Nombre d'étudiants: "))

    # 1. Saisir les noms de n étudiants
    liste_etudiants = saisir_etudiants(n)
    
    # 2. Afficher la liste des étudiants
    affichier_etudiants(liste_etudiants)
    
    # 3. Saisir les notes des étudiants (3 matières)
    notes = saisir_notes(liste_etudiants)
    
    # 4. Calcule les moyennes des étudiants
    moyennes = calcule_moyenne(notes)
    
    # 5. Calcule le rang des étudiants suivant les moyennes
    
    # 6. Sauvegarder les notes des étudiants dans un fichier
    
    # 7. Afficher la liste des étudiants avec leurs notes depuis le fichier.
    


if __name__ == "__main__":
    main()
