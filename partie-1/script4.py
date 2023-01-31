# coding : utf-8

def main():
    # nom = input('Nom: ')
    # pays = input('Pays: ')
    # age = int(input('Age: '))
    # taille = float(input('Taille: '))
    nom = 'John Doe'
    pays = 'USA'
    age = 35
    taille = 1.79
    majeur = True
    
    print(nom)
    print('Nom:', nom)
    print('Pays: {}'.format(pays))
    print(f'Age: {age}')
    print('Taille:', taille)
    print('Majeur:', majeur)

if __name__ == "__main__":
    main()
