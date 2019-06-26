#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import re
from tqdm import tqdm
import glob
import os
import json
import numpy as np


path_from = "C:/Users/Elina/NS/Project 2/Data1"
path_to = "C:/Users/Elina/NS/Project 2/"


with open(path_to+'articles_wos.json', 'r') as f:
    articles = json.load(f)


journals = [articles[0]["source"]]
for i in tqdm(range(1, len(articles))):
    #print(articles[i]["source"])
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

