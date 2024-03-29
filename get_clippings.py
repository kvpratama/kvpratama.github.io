﻿import numpy as np
import pdb

keyword = '21 Lessons for the 21st Century'

with open('My Clippings.txt', 'r', encoding='UTF-8', newline='') as file:
    data = file.read()

arr = data.split('==========')
found = []

for a in arr:
    if keyword in a:
        try:
            clean = a.split('Your Highlight on ')[1:][0].replace('\r\n\r\n', '\r\n> ')
        except:
            pass

        # replace Em Dash '—' with '-'
        clean = clean.replace("—", "-")
        # replace En Dash '–' with '-'
        clean = clean.replace("–", "-")

        # replace ’ with "'"
        clean = clean.replace("’", "'")
        clean = clean.replace("ʼ", "'")

        # replace ” with '"'
        clean = clean.replace('”', '"')
        # replace “ with '"'
        clean = clean.replace('“', '"')

        clean = clean.replace('ê', 'e')
        clean = clean.replace('é', 'e')


        found.append(clean)

np.savetxt(f"{keyword}.txt", found, fmt='%s',delimiter ='==========')

print(f"Found {len(found)} highlight of {keyword}")
print(f"Saved to {keyword}.txt")
#pdb.set_trace()