#!/usr/bin/env python
# coding : utf-8

'''
    Structures de données: Les listes
    Author : Joseph
    Date : 21.02.2023
'''

def main():
    '''les listes'''
    participants = ["Kpatcha", "Hervé", "Seydou", "Rachid"]

    print('Premier élément:', participants[0])
    print('Dernier élément:', participants[-1])
    print('Trois premier élément:', participants[:3])

    print(participants)
    participants.sort(reverse=True)
    print(participants)
    
    for participant in participants:
        print(participant)
        
    for index, participant in enumerate(participants):
        print(index, participant)

if __name__ == "__main__":
    main()
