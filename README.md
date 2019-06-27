# Network Science

**Done by:** Aunts Edward, Pershin Maksim, Sukhanova Elina

This repository contains:
* WoS_scraping_research.ipynb - Research notebook with some experiments and tries of 
downloading articles from WoS website;
* Scraping_script.py - Script for automatic articles data downloading with specified
delay time between downloads;
* Parsing_articles.py - Script for articles data parsing from raw format to json;
* Parsing_journals.py - Script for journals data parsing from raw format to json;
* Parsing_authors.py - Script for authors data parsing from raw format to json.

# Report

### Scraping

Web of Science (WoS) - a subscription-based platform that gives an access to several 
databases: articles, journals etc. Core business of this platform is based on the
intellectual properties and data. It leads to high quality protection of this 
platform from any scraping approaches.

At the beginning we created a function to connect WoS from python script for 
automatic processing of sign-in steps. It is important for future discussion 
that connection is possible only through HSE website and with a personal key-pair. 
By using selenium package by xpath we found login and password forms, input data
into forms and submit to the main page of WoS:

![alt text](https://vk.com/doc167940720_508176993)



**First try (unsuccessful)**

**Second try (partially successful)**



### Parsing
