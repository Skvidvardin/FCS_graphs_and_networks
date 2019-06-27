#!/usr/bin/env python
# coding: utf-8
from tqdm import tqdm
import json

"""
In the script below unique titles of parsed articles are being extracted from json file.
"""

print('Inpit path to folder for data and results:')
path_to = input()

with open(path_to+'articles_wos.json', 'r') as f:
    articles = json.load(f)


journals = [articles[0]["source"]]
for i in tqdm(range(1, len(articles))):
    F = False
    for j in range(len(journals)):
        if (articles[i]["source"] == journals[j])|(articles[i]["source"] == 'NaN'):
            F = True
            break
    if not(F):
        journals.append(articles[i]["source"])


for i in tqdm(range(len(journals))):
    journals[i] = journals[i].replace("\n   ", " ")


with open(path_to+'journals.txt', 'w') as f:
    for item in journals:
        f.write("%s\n" % item)

