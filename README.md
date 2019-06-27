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
platform from any scraping approaches. Number of articles that platform contains: 90 million.

At the beginning we created a function to connect WoS from python script for 
automatic processing of sign-in steps. It is important for future discussion 
that connection is possible only through HSE website and with a personal key-pair. 
By using selenium package by xpath we found login and password forms, input data
into forms and submit to the main page of WoS:

![alt text](https://psv4.userapi.com/c848136/u167940720/docs/d9/cb0266761286/image_2019-06-27_03-47-15.png?extra=WuBJwI4ScgoZ_UxqLjLB9Dk9mfdDdlDRNEpyFw8KEjYo1CfIetePCF4ojYlrRRboQSnS7XbkJuKIWdPPa_zrJrm6idalmKVyzMDefvcDW4S0stIvdmY1eCnHT0g2je73bP2HVzU6M6o70lDHI00IZXoCCr4)

Website not allows to scroll over the whole database or query a database for all 
records output (checked). WoS has only function to query and output only part of
database. Therefore it is not possible to go over records only once without
checking for repetitions.

After a search query we have a such representation:

![alt text](https://psv4.userapi.com/c848436/u167940720/docs/d11/95e7d0687d60/image_2019-06-27_04-12-00.png?extra=qn1HHwEo_ssL1o-KrhPrgT-9k9pdLO_pnTFgl2ybHrNYWYl6WYJr73drz64eiHX8Qqi2wvYrYdaQYZY8yVr3ufmQ7LFZfk8lmT1Nm1itsEx1BZaj9AsGatPRsSr2vaihII82F0f3UIUdfiBFtbNdnRLLDfI)

**First try (unsuccessful)**

Firstly we found that even with visual limit of scroll over pages ("1 of 10,000" in picture)
there possible to 


**Second try (partially successful)**


### Parsing
