from SearchEngineScrapy.utils.searchengines import SearchEngine

class SearchEngineURLs:
    searchQuery = None
    searchEngine = None
    searchEngineBaseUrl = None
    pages = 0
    currentPage = 0

    def __init__(self, searchQuery, searchEngine, pages):
        self.searchQuery = searchQuery
        self.searchEngine = searchEngine
        self.pages = pages
        self.searchEngineBaseUrl = SearchEngine[self.searchEngine]
    
    def __iter__(self):
        return  self

    def _currentUrl(self):
        return self.searchEngineBaseUrl.format(self.searchQuery, str(self.currentPage  * 10))

    def next(self):
        if self.currentPage < self.pages:
            url =  self._currentUrl()
            self.currentPage = self.currentPage + 1
            return  url
        raise StopIteration