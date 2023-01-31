#!/usr/bin/env python
# coding : utf-8

'''
    Authentification
    Author : Joseph
    Date : 21.02.2023
'''

from getpass import getpass

PASSWORD = 'Togo2023'

def main():
    '''authentification'''
    password = getpass('Enter your password:')

    if password == PASSWORD:
        print('Access authorized')
    else:
        print('Access denied')

if __name__ == "__main__":
    main()
