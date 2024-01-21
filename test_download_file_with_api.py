import requests


url = "https://www.selenium.dev/images/sponsors/browserstack.png"

response = requests.get(url, allow_redirects=True)

'''
file = open("browserstack.png", 'wb')
file.write(response.content)
file.close()
'''


with open('browserstack.png', 'wb') as f:
    f.write(response.content)


