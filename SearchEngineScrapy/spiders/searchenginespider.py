from scrapy.selector import Selector
from scrapy.spider import Spider

from SearchEngineScrapy.utils.searchengines import SearchEngineResultSelector
from SearchEngineScrapy.utils.searchenginepages import SearchEngineURLs
from SearchEngineScrapy.utils.utilities import Utilities

import os
import subprocess
import requests

class SearchEngineScrapy(Spider):
    name = "SearchEngineScrapy"

    allowed_domains = ['bing.com','google.com']
    start_urls = []

    searchQuery = None
    searchEngine = None
    fileType = None
    selector = None
    downloadFolder = None
    downloadFiles = False

    def __init__(self, searchQuery, fileType, downloadFolder = "", searchEngine = "bing", pages = 3, *args, **kwargs):
        super(SearchEngineScrapy, self).__init__(*args, **kwargs)
        self.searchQuery = searchQuery.lower()
        self.fileType = fileType.lower()
        if fileType is not None:
            self.searchQuery = "{0} filetype:{1}".format(self.searchQuery, self.fileType)
        self.searchEngine = searchEngine.lower()
        self.pages = int(pages)
        if downloadFolder == "":
            self.downloadFiles = False
        else:
            self.downloadFiles = True
            if os.path.isdir(downloadFolder):
                self.downloadFolder = downloadFolder
            else:
                if not os.path.isdir(os.path.join(os.getcwd(), "downloads")):
                    os.makedirs(os.path.join(os.getcwd(), "downloads"))
                self.downloadFolder = os.path.join(os.getcwd(), "downloads")

        pageUrls = SearchEngineURLs(self.searchQuery, self.searchEngine, self.pages)
        self.selector = SearchEngineResultSelector[self.searchEngine]

        for url in pageUrls:
            self.start_urls.append(url)

    def parse(self, response):
        for url in Selector(response).xpath(self.selector).extract():
            if self.searchEngine == "google":
                url = "https://www.google.com{}".format(url)
            urlInfo = requests.head(url, allow_redirects=True, verify=False)
            url = urlInfo.url
            if Utilities().is_filetype(self.fileType, urlInfo):
                fname = Utilities().get_filename(self.fileType, url, urlInfo)
                if self.downloadFiles:
                    fname = os.path.join(self.downloadFolder, fname)
                    subprocess.call(["curl", "-o", fname, url])
                yield { 'url': url }
        pass