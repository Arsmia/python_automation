import os

os.path.getsize('browserstack.png')
print(os.path.getsize('browserstack.png'))

os.path.abspath(__file__)
print(os.path.abspath(__file__))   #find absolute path to this file

os.path.dirname(__file__)
print(os.path.dirname(__file__))


print(os.path.dirname(os.path.abspath(__file__)))


'''
path = "/Users/sviat/PycharmProjects/pythonProject/text.txt"
os.remove(path)
print("txt file is removed")
'''