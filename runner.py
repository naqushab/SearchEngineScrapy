import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from SearchEngineScrapy.spiders.searchenginespider import SearchEngineScrapy
from SearchEngineScrapy.utils.utilities import Utilities

from gooey import Gooey, GooeyParser

import os
import urlparse, urllib


@Gooey( program_name="Search and Download PDFs", default_size=(650, 500), image_dir='images')
def arg_parse():
    parser = GooeyParser()
    g = parser.add_argument_group(
        gooey_options={
            'show_border': True,
            'columns': 1 
        }
    )

    g.add_argument(
        'searchquery',
        metavar='Search Query',
        gooey_options={
            'validator': {
                'test': 'user_input != ""',
                'message': 'Please enter a search keyword.'
            }
        })
    
    h = parser.add_argument_group(
        gooey_options={
            'columns': 2 
        }
    )

    h.add_argument(
        'searchengine',
        metavar='Search Engine',
        widget='Dropdown',
        choices=['Bing', 'Google'],
        default='Bing',
        gooey_options={
            'validator': {
                'test': 'user_input != "Select Option"',
                'message': 'Choose a search engine from the list'
            }
        })
    
    h.add_argument(
        'pages',
        metavar='Pages to Crawl',
        type=int,
        default=2,
        gooey_options={
            'validator': {
                'test': '0 < int(user_input)',
                'message': 'Enter page count > 0'
            }
        })
    
    downloadsPath = os.path.join(os.path.expanduser('~'), 'Downloads')
    h.add_argument(
        dest='downloadfolder',
        default=downloadsPath,
        metavar='Download Location',
        widget='DirChooser')
    
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = arg_parse()
    project_settings = get_project_settings()
    shouldDownload = 'Yes'
    filetype = 'pdf'

    fileName = "{0}_{1}".format('Results', args.searchquery)
    fileName = Utilities().clean_filename(fileName, 'csv', True)
    
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