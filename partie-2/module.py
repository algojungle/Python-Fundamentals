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

import json

# Constantes
NB_NOTES = 3


def saisir_liste_etudiants(effectif):
    etudiants_liste = []
    for i in range(effectif):
        etud = input(f'Name of student n°{i+1}: ')
        etudiants_liste.append(etud)
        
    return etudiants_liste

def afficher_effectif(etudiants_liste):
    # for etudiant in etudiants_liste:
    #     print(etudiant)
    for i, etudiant in enumerate(etudiants_liste):
        print(i+1, etudiant)

def saisir_notes(etudiants_liste):
    notes = []
    for i, etudiant in enumerate(etudiants_liste):
        print(f'Etudiant n°{i+1} : {etudiant}')
        notes_etud = []
        for j in range(NB_NOTES):
            note = int(input(f'Note Matière{j+1} : '))
            notes_etud.append(note)
        notes.append(notes_etud)

    return notes

def calculer_moyenne(notes_liste):
    moyennes = []
    for i in range(len(notes_liste)):
        moy_etud = 0
        for j in range(NB_NOTES):
            moy_etud += notes_liste[i][j]
        moy_etud = moy_etud / NB_NOTES
        moyennes.append(round(moy_etud, 2))

    return moyennes

def calcul_rang(moyennes_liste):
    rang = list(range(len(moyennes_liste)))

    changed = True
    while changed:
        changed = False
        for i in range(len(moyennes_liste)-1):
            if moyennes_liste[i] < moyennes_liste[i+1]:
                moyennes_liste[i], moyennes_liste[i+1] = moyennes_liste[i+1], moyennes_liste[i]
                changed = True
                rang[i], rang[i+1] = rang[i+1], rang[i]
    
    return rang


def exporter_etudiant(etudiants_liste, notes_liste, moyennes_liste, rangs, filename):
    results = []
    
    for i in rangs:
        res = {
            'nom': etudiants_liste[i],
            'notes' : notes_liste[i],
            'moyenne': moyennes_liste[i],
            'rang' : i
        }
        results.append(res)
        
    # Write
    with open(filename, 'w') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)


def charger_etudiant(filename):
    # Read
    with open(filename, 'r') as f:
        etudiants = json.load(f)
        
    return etudiants
