import os

with open("Resources/text.txt", "w") as file:
    file.write("abc\ndef\nghi")

with open("Resources/text.txt") as file:
    for row in file:
        print(row)

'''
with open('text.txt', 'a') as file:
    file.write('\nwyz')
'''

