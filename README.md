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
there possible to iterate over all (38,672,622) results inside article. After this remark
with selenium was created a script to scrape necessary information from article page. 
At this step we faced such as issues as: changeable xpaths, different numbers of authors and 
keywords, slow page loading (each such page loads min 0.2 sec ~ 208 days for one loop over
all articles) 
and etc (details about problems are in *.ipynb file). Article page example:

![](https://psv4.userapi.com/c848032/u167940720/docs/d8/6da13a161029/image_2019-06-27_04-36-10.png?extra=BIeYHXFi21yeBUreGdNd3cKFpw84QLLuh0piktVkEAz8J89_PVTD_OowOgtNthWm3eSzFvudssuk0OVbLd6OVGbbsWPnt4QWJDITmfP-Icev7Sb7rA_K0jo_kpKl5tBo-GZ_MYsY7ZL8DhTyLVn50gS2KtM)

We overcome these issues and created
high detailed review of scraped and parsed articles, but WoS blocked all quires for account
to articles with id > 1000 after several (each time different) iterations. Then we designed a 
system of different IPs VPN servers connect but WoS was blocking by login not IP.

Last attempt was to use login in from different machines with different IPs, but it also failed.
HSE gave a permanent block to account (now Maksim Pershin does not have an account to connect 
HSE e-library resources). 

**Second try (partially successful)**

After a discussion of required information we decided to use standard WoS "Export..." function:

![](https://psv4.userapi.com/c848036/u167940720/docs/d3/28e2b7de7cd5/image_2019-06-27_04-53-15.png?extra=DndotBtBOf6nO4NTMNIPAJpRrw3iDJK2AmA3gEK5v5W5jCiS4JrcQPHRL5lBQH9TwSkQG1e57kBkkHhevdvisLtuWuufdnKpI6StCz36IV1JHrSz9RPQEYqoivDqLW8zvXLqCSCLEniHk_6zYd8A2qUh1sg)

Now we could collect ~99,000 articles per query by looping over different records.
It takes approximately 4-5 hours to collect data by one search query. Main interesting issue
that we faced while tried to scrape this elements was divs protection with stochastic components.
It required to use additional html text search tricks.

### Parsing
After "second try" operation of scraping data we had N HTML files with data about articles:

![](https://psv4.userapi.com/c848232/u167940720/docs/d8/45863a3b4de6/image_2019-06-27_08-03-29.png?extra=lNjHIBpFz8tO-M-0_B91-k9ayviqbY6YaHP-LN_BnOkl16OdTJP34nl78LwEME5jDzyMAEAyLPWwPxx5plI4Xgm6WftGeTho8wM4W3HG5hPlGutpLR6ifcvm279otltGyVQT8is51QQYl7V8CcEL4bK8GpM)

We compared this template with an article’s wos page and founded out that:
* "AU" stands for authors;
* "TI" stands for title;
* "DA" stands for date;
* "SO" stands for source;
* "PG" stands for number of pages;
* "TC" stands for number of citations;
* "DI" stands for DOI;
* "AB" stands for abstract (short description);
* "DE" stands for authors keywords;
* "LA" stands for language;
* "PU" stands for publisher;
* "CT" stands for conference name;
* "CY" stands for conference date;
* "CR" stands for work links.

Unfortunately, we do not have authorID and link information in our downloaded HTML articles. 
Also, WoS does not provide information about sponsors.
We parsed downloaded html articles information via BeautifulSoup module.
When we parse new articles, we also check their uniqueness. 
This is done in “Parsing_articles.py” script.

During our project we had two additional tasks: to parse information about journals and authors. 
To do so we should first get a list of all journals mentioned in parsed articles. 
So, we got journals title from json articles and dropped any duplicates. 
This is done in “Parse_journals.py” script.

For authors created a script "Parsing_authors.py", that takes as an input the 
folder with all HTML pages (each contains 500 articles). 
For each page the following info is available:
 * Name;
 * Institution;
 * Coauthors;
 * Papers with coauthors;
 * Number of papers.

To identify researches and prevent collisions - the pair of Name and Surname + first part of institution 
(till the comma) was used. 
Script iterates over articles and  creates a value for each author;
It checks  whether a researched is already added or not, and if he was added to dict previously,
then he is info is updated (coauthors, articles list, number of publications).

### Results

