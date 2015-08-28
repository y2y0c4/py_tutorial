import urllib.request
import re
import os
import pprint
url = 'http://webtoon.daum.net/webtoon/viewer/32683'
res = urllib.request.urlopen(url)
html = res.read()

#pprint.pprint(html)

pattern = b'''img src="(http://i1.cartoon.daumcdn.net/svc/image/U03/cartoon/)(.*?)"'''

match=re.findall(pattern, html)

pprint.pprint(match)
wanted_str = str(match[0][0])[2:-1]+str(match[0][1])[2:-1]
print(wanted_str)
os.system('wget '+ wanted_str)