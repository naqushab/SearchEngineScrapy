import scrapy
from scrapy.crawler import CrawlerProcess

from SearchEngineScrapy.spiders.searchenginespider import SearchEngineScrapy

process = CrawlerProcess()

process.crawl(SearchEngineScrapy, searchquery="ascii", filetype=".pdf")
process.start()