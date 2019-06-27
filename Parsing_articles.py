#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import re
from tqdm import tqdm
import glob
import os
import json

"""
In the script below the html pages with articles are being parsed. It takes as an input the 
folder with all html pages (each contains 500 articles). For each page the following info is available:
    * authors
    * title
    * date
    * source
    * number of pages
    * number of citations
    * DOI
    * short description
    * keywords
    * language
    * publisher
    * conference name
    * conference date
    * work links

AuthorID, link information and sponsors are not avaliable

Script iterates over articles and parse them;
It drops duplicates afterall.
"""

print('Inpit path to folder with files to parse:')
path_from = input()
print('Inpit path to folder for results:')
path_to = input()

def parse_article(article):
    d = {}

    try:
        d['authors'] = article.find(text="AU ").find_next().get_text().split("\n   ")
    except:
        d['authors'] = "NaN"

    try:
        d['title'] = article.find(text="TI ").find_next().get_text().replace('\n   ', ' ')
    except:
        d['title'] = "NaN"

    try:
        d["year"] = article.find(text="DA ").find_next().get_text()
    except:
        d["year"] = "NaN"

    try:
        d['source'] = article.find(text="SO ").find_next().get_text()
    except:
        d['source'] = 'NaN'

    try:
        d['pagesNumber'] = article.find(text="PG ").find_next().get_text()
    except:
        d["pagesNumber"] = 'NaN'

    try:
        d['citationsNumber'] = article.find(text="TC ").find_next().get_text()
    except:
        d['citationsNumber'] = 'NaN'

    try:
        d['DOI'] = article.find(text="DI ").find_next().get_text()
    except:
        d['DOI'] = 'NaN'

    try:
        d['shortDescription'] = article.find(text="AB ").find_next().get_text().split('\n')[0]
    except:
        d['shortDescription'] = 'NaN'

    try:
        d['keywords'] = re.split(';  |; |;\n  ', article.find(text="DE ").find_next().get_text())
        for i in range(len(d['keywords'])):
            d['keywords'][i] = d['keywords'][i].replace('\n   ', ' ')
    except:
        d['keywords'] = 'NaN'

    try:
        d['documentLang'] = article.find(text="LA ").find_next().get_text()
    except:
        d['documentLang'] = 'NaN'

    try:
        d['publisher'] = article.find(text="PU ").find_next().get_text()
    except:
        d['publisher'] = 'NaN'

    try:
        name = article.find(text="CT ").find_next().get_text().replace('\n   ', ' ')
    except:
        name = 'NaN'
    try:
        year = article.find(text="CY ").find_next().get_text()
    except:
        year = 'NaN'
    d["conference"] = {name:year}

    try:
        d['workLinks'] = article.find(text="CR ").find_next().get_text().split('\n   ')
    except:
        d['workLinks'] = 'NaN'
    return(d)


parsed = []
for filename in tqdm(glob.glob(os.path.join(path_from, '*.html'))):
    soup = BeautifulSoup(open(filename, encoding='utf-8'), "html.parser")   
    parsed.append(parse_article(soup))
    lines = soup.find_all("hr")
    for i in range((len(lines)-1)): 
        parsed.append(parse_article(lines[i].find_next()))

parsed_new = parsed


with open(path_to+'articles_wos.json') as f:
    parsed = json.load(f)


F = False
for i in tqdm(range(len(parsed_new))):
    F = False
    for j in range(len(parsed)):
        if parsed_new[i]["DOI"] == parsed[j]["DOI"]:
            F = True
            break
    if not F:
        parsed.append(parsed_new[i])


FINAL = []
FINAL.extend(parsed)
with open(path_to+'articles_wos.json', 'w') as f:
    json.dump(FINAL, f)

