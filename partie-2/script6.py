

'''
    Files Opening Modes
        - w : write
        - r : read
        - a : append
'''


texte = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

FILE = 'fichier1.txt'

# Open the file
# f = open(FILE, mode='w')
f = open(FILE, mode='a')

# Write in the file
f.write(texte)

# Close the file
f.close()


# Open the file
f = open(FILE, mode='r')

# read file content
print(f.read())
# print(f.readlines())

# Close the file
f.close()