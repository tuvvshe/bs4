import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

link = input('Enter loc: ')
html = urllib.request.urlopen(link).read().decode()
print('Retrieving', link)
print('Retrieving', len(html), 'charcters')

cn = 0
sm = 0
data = ET.fromstring(html)
tags = data.findall('comments/comment')

for tag in tags:
    cn += 1
    sm += int(tag.find('count').text)

print('Count:', cn)
print('Sum:',sm)

#http://py4e-data.dr-chuck.net/comments_1890065.xml
