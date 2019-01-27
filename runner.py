import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from SearchEngineScrapy.spiders.searchenginespider import SearchEngineScrapy

from gooey import Gooey, GooeyParser

import os
import urlparse, urllib


@Gooey( program_name="Search Engine Crawler", default_size=(850, 600), required_cols=3)
def arg_parse():
    parser = GooeyParser(description='Search and Download PDFs')

    parser.add_argument(
        'searchquery',
        metavar='Search Query',
        gooey_options={
            'validator': {
                'test': 'user_input != ""',
                'message': 'Please enter some search query'
            }
        })
    
    parser.add_argument(
        'searchengine',
        metavar='Select Search Engine',
        widget='Dropdown',
        choices=['Bing', 'Google'],
        default='Bing',
        gooey_options={
            'validator': {
                'test': 'user_input != "Select Option"',
                'message': 'Choose a search engine from the list'
            }
        })
    
    parser.add_argument(
        'pages',
        metavar='Enter number of pages to crawl',
        type=int,
        default=2,
        gooey_options={
            'validator': {
                'test': '0 < int(user_input)',
                'message': 'Enter page count > 0'
            }
        })
    
    parser.add_argument(
        dest='downloadfolder',
        metavar='Output Folder',
        widget='DirChooser',
        help='Enter where to save results and files')
    
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = arg_parse()
    project_settings = get_project_settings()
    shouldDownload = 'Yes'
    filetype = 'pdf'
    fileName = 'results_crawled.csv'
    filePath = os.path.join(args.downloadfolder, fileName)
    feedPath = urlparse.urljoin('file:', urllib.pathname2url(filePath))
    project_settings.overrides['FEED_FORMAT'] = 'csv'
    project_settings.overrides['FEED_URI'] = feedPath
    process = CrawlerProcess(project_settings)
    if shouldDownload == 'No':
        process.crawl(SearchEngineScrapy, searchquery=args.searchquery, filetype=filetype, pages=args.pages, searchengine=args.searchengine)
    else:
        process.crawl(SearchEngineScrapy, searchquery=args.searchquery, filetype=filetype, pages=args.pages, searchengine=args.searchengine, downloadfolder=args.downloadfolder)
    process.start()