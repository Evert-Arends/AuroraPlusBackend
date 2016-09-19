import requests

# sending info to the API
user = 'Berm'
url = ('http://127.0.0.1:8000/data/%s' % user)

content = requests.post(url, data={'data': 'Testing'})
# content = requests.get(url)
print (content.content)



