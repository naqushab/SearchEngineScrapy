SearchEngine = {
    'google': 'https://www.google.com/search?q={0}&start={1}',
    'bing': 'http://www.bing.com/search?q={0}&first={1}',
    'ask' : 'http://www.ask.com/web?q={0}&page={1}',
    'baidu' : 'https://www.baidu.com/s?wd={0}&pn={1}',
    'yahoo' : 'https://search.yahoo.com/search;?p={0}&b={1}',
    'yandex' : 'https://www.yandex.com/search/?text={0}&p={1}'
}

SearchEngineResultSelector = {
    'google': '//h3/a/@href',
    'bing':'//h2/a/@href',
    'ask': '//div[@class="PartialSearchResults-item-title"]/a/@href',
    'baidu': '//h3/a/@href',
    'yahoo' : '//h3/a/@href',
    'yandex' : '//h2/a/@href'

}