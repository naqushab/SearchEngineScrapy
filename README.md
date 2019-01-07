# SearchEngineScrapy - Scrape data from Google.com, Bing.com

[![Python 2](https://img.shields.io/badge/Python-2.7-brightgreen.svg)](https://docs.python.org/2) [![Travis](https://img.shields.io/travis/rust-lang/rust.svg)]()

## Intro

SearchEngineScrapy is a web crawler and scraper for scraping data off
various search engines such as Google.com, Bing.com. It is based on Python Scrapy project and is developed
using Python 2.7


## Setup (Windows)
```
    git clone https://github.com/naqushab/SearchEngineScrapy.git
    cd SearchEngineScrapy
    virtualenv --python=2 venv
    venv\Scripts\activate
    pip install -r requirements.txt
```

## Setup (Mac)

```
    git clone https://github.com/naqushab/SearchEngineScrapy.git
    cd SearchEngineScrapy
    virtualenv -p python venv
    source venv/bin/activate
    pip install -r requirements.txt
```

## Usage

***Prefix*** : `-a`

**Params**

searchQuery="<your search query>" [Required Parameter] 

fileType="<filetype you want to search for>" [Required Parameter : Example 'pdf', 'csv' etc]

searchEngine="<your search engine>" [Options: Google/Bing/Ask/Yandex/Baidu/Yahoo] [Optional  Parameter] [Default: Bing] 

pages=<pages to crawl> [Number of pages to crawl] [Optional Parameter : Default: 3]

***Prefix*** : `-o`

***Params***

<filename> [Output the resulta to a file] [Optional Parameter] [Supported:json/jsonl/csv/xml]


### Examples 
```
scrapy crawl SearchEngineScrapy -a searchQuery="Adobe" -a fileType="pdf"
scrapy crawl SearchEngineScrapy -a searchQuery="Adobe" -a fileType="pdf" -o filename.json 
scrapy crawl SearchEngineScrapy -a searchQuery="Adobe" -a fileType="pdf" -a searchEngine="Google" -o filename.xml 
scrapy crawl SearchEngineScrapy -a searchQuery="Adobe" -a fileType="pdf" -a searchEngine="Google" -a pages=5 -o filename.csv
```


## TODO

-   Add support for DDG
-   Ability to export to various formats (currently limited to JSON,
    JSONLINES, CSV, XML)
-   Contributing section
