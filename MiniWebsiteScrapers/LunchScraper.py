# -*- coding: utf-8 -*-

import urllib.request
import re
import pyperclip

url = 'http://www.vibenshuset.dk/info/'

replacements = {
	"<br>": " "
}

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

# <div class="tab-pane active" id="man">Spaghetti bolognese med pesto salat, stegte cherrytomater, parmesan og salvie</div>

regexResults = re.findall(r'<div class="tab-pane( active)?" id="(...)">(.*?)</div>', str(respData, 'utf-8'))

lines = [str(entry[2]) for entry in regexResults]

lines_fixed = []
for line in lines:
	for key in replacements:
		line = line.replace(key, replacements[key])
	lines_fixed.append(line)

finalResults = "\n".join(lines_fixed)

print("Copied Lunch:\n\n" + finalResults + "\n")
pyperclip.copy(finalResults)
