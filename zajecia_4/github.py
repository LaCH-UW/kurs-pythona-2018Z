import requests

r = requests.get('https://api.github.com/users/{user}'.format(user='piotrkasprzyk'))
j_data = r.json()

print(j_data)

print(j_data['name'])
print(j_data['url'])
print(j_data['avatar_url'])


from PIL import Image  # ta linijka wymaga biblioteki pillow, która również powinna przyjść z anacondą
from io import BytesIO  # a to jest biblioteka standardowa

avatar_url = j_data['avatar_url']
r = requests.get(avatar_url)
i = Image.open(BytesIO(r.content))
i.show()
