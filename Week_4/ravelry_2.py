from bs4 import BeautifulSoup
import requests

client = requests.Session()

email = 'itesser@gmail.com'
password = '1ceT4me8*'
home_url = 'https://www.ravelry.com/'
login_url = 'https://www.ravelry.com/account/login'

with requests.Session() as s:
    req = s.get(login_url).text
    html = BeautifulSoup(req, 'html.parser')
    token = html.find("input", {'name':'authenticity_token'}).attrs['value']

payload = {
    'authenticity_token' : token,
    'origin' : 'splash',
    '_splash' : '2002',
    'return_to': '',
    'user[login]': email,
    'user[password]' : password
}

res = s.post(login_url, data=payload)

print(res.url)