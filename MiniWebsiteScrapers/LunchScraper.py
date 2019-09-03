# -*- coding: utf-8 -*-

import urllib.request
import re
import pyperclip

url = 'http://www.vibenshuset.dk/info/'

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

# <div class="tab-pane active" id="man">Spaghetti bolognese med pesto salat, stegte cherrytomater, parmesan og salvie</div>

regexResults = re.findall(r'<div class="tab-pane( active)?" id="(...)">(.*?)</div>', str(respData, 'utf-8'))

finalResults = "\n".join(str(entry[2]) for entry in regexResults)

print("Copied Lunch:\n\n" + finalResults + "\n")
pyperclip.copy(finalResults)
