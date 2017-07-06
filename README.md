# SearchEngineScrapy - Scrape data from Google.com, Bing.com, Baidu.com, Ask.com, Yahoo.com, Yandex.com,  

 [![Python](https://img.shields.io/badge/Python-2.7%2C%203.6-brightgreen.svg)](http://www.python.org/download/) [![Travis](https://img.shields.io/travis/rust-lang/rust.svg)]()

## Intro

SearchEngineScrapy is a web crawler and scraper for scraping data off
various search engines such as Google.com, Bing.com, Yahoo.com,
Ask.com, Baidu.com, Yandex.com It is based on Python Scrapy project and is developed
using Python 2.7

It is also compatible with Python 3


## Setup

```
    virtualenv --python="which python" env
    env/bin/activate
    git clone hhttps://github.com/naqushab/SearchEngineScrapy.git
    cd SearchEngineScrapy
    pip install -r requirements.txt
```

## Usage

**Parameters** 
```
searchQuery="<your search query>" [Required Parameter] 

searchEngine="<your search engine>" [Options: Google/Bing/Ask/Yandex/Baidu/Yahoo] [Optional  Parameter] [Default: Bing] 

pages=<pages to crawl> [Number of pages to crawl] [Optional Parameter] Default: 3] 

-o <filename> [Output the resulta to a file] [Optional Parameter] [Supported:json/jsonl/csv/xml]
```

**Examples** 
```
scrapy crawl SearchEngineScrapy -a searchQuery="I'm Batman"
scrapy crawl SearchEngineScrapy -a searchQuery="I'm Batman" -o filename.json 
scrapy crawl SearchEngineScrapy -a searchQuery="I'm Batman" -a searchEngine="Google" -o filename.xml 
scrapy crawl SearchEngineScrapy -a searchQuery="I'm Batman" -a searchEngine="Google" -a pages=5 -o filename.csv
```


## TODO

-   Add support for DDG
-   Ability to provide parameter of what to save
-   Ability to export to various formats (currently limited to JSON,
    JSONLINES, CSV, XML)
-   Contributing section