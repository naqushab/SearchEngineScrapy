SearchEngineScrapy - Scrape data from Google.com, Bing.com, Baidu.com, Ask.com, DuckDuckGo.com
===============================================

Intro
-----
SearchEngineScrapy is a web crawler and scraper for scraping data off various search engines such as Google.com, Bing.com, DuckDuckGo, Ask.com, Baidu
It is based on Python Scrapy project and is developed using Python 2.7

It is also compatible with Python 3

Licensing
---------
TODO

Setup
-----

::

    virtualenv --python="which python" env
    env/bin/activate
    git clone hhttps://github.com/naqushab/SearchEngineScrapy.git
    cd SearchEngineScrapy
    pip install -r requirements.txt

Usage
------------------

**Parameters**
::
    searchQuery="<your search query>"  [Required Parameter]
    searchEngine="<your search engine>"  [Options: Google/Bing]  [Optional Parameter] [Default: Bing]
    pages=<pages to crawl>  [Number of pages to crawl]  [Optional Parameter] [Default: 3]
    -o <filename> [Output the resulta to a file] [Optional Parameter] [Supported:json/jsonl/csv/xml]

**Examples**
::
    scrapy crawl SearchEngineScrapy -a searchQuery="I'm Batman" -o filename.json
    scrapy crawl SearchEngineScrapy -a searchQuery="I'm Batman" -a searchEngine="Google" -o filename.xml
    scrapy crawl SearchEngineScrapy -a searchQuery="I'm Batman" -a searchEngine="Google" -a pages=5 -o filename.csv


TODO
----

-  Add support for DDG
-  Add support for Baidu
-  Add support for Ask.com
-  Add support for Chacha.com
-  Ability to provide parameter of what to save
-  Ability to export to various formats (currently limited to JSON, JSONLINES, CSV, XML)


Contributing
---------
TODO
