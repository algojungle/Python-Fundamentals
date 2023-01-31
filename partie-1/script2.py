#!/usr/bin/env python
# coding : utf-8

'''
    Calculate the age of the user based on the birth date
    Author : Joseph
    Date : 21.02.2023
'''

ANNEE = 2023

def main():
    '''main function prints age'''
    birth_year = int(input('Enter your birth year:'))
    age = ANNEE - birth_year
    print("Your age is", age)

if __name__ == "__main__":
    main()
