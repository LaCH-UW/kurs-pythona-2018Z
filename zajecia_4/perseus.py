import requests
from lxml import etree

response = requests.get('http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus%3Atext%3A1999.01.0133%3Abook%3D1%3Acard%3D1')
root = etree.fromstring(response.content)
print(root)
print(root.tag)
print([c.tag for c in root])
print([c.tag for c in root[0]])
print([c.tag for c in root[0][0]])
print([c.tag for c in root[0][0][0]])
print(root[0][0][0][2].text)
