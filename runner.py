import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from SearchEngineScrapy.spiders.searchenginespider import SearchEngineScrapy

from gooey import Gooey, GooeyParser

import os
import urlparse, urllib


@Gooey( program_name="Search Engine Scrapy", default_size=(850, 600))
def arg_parse():
    parser = GooeyParser(description='Crawl Search Engine Results and optionally download them')

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
        'filetype',
        metavar='Select File Type to search for',
        widget='Dropdown',
        choices=['pdf', 'csv', 'zip', 'doc', 'docx', 'jpeg', 'png'],
        default='pdf',
        gooey_options={
            'validator': {
                'test': 'user_input != "Select Option"',
                'message': 'Choose a filetype from the list'
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
        'output_filename',
        metavar='Output Filename',
        help='For file with crawled URLs dumped (without extension)',
        default='urls',
        gooey_options={
            'validator': {
                'test': 'user_input != ""',
                'message': 'Enter Output Filename'
            }
        })
    parser.add_argument(
        'output_filetype',
        metavar='Output File Type',
        widget='Dropdown',
        choices=['json', 'jsonl', 'csv', 'xml'],
        help='File type of the output file',
        default='csv',
        gooey_options={
            'validator': {
                'test': 'user_input != "Select Option"',
                'message': 'Choose a filetype from the list'
            }
        })
    
    parser.add_argument(
        dest='downloadfolder',
        metavar='Output Folder',
        widget='DirChooser',
        help='Enter where to save results and files')

    parser.add_argument(
        dest='shouldDownload',
        metavar='Want to Download Files?',
        widget='Dropdown',
        choices=['Yes', 'No'],
        default='No',
        gooey_options={
            'validator': {
                'test': 'user_input != "Select Option"',
                'message': 'Select Yes/No'
            }
        })
    
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = arg_parse()
    project_settings = get_project_settings()
    fileName = args.output_filename + '.' +  args.output_filetype
    filePath = os.path.join(args.downloadfolder, fileName)
    feedPath = urlparse.urljoin('file:', urllib.pathname2url(filePath))
    project_settings.overrides['FEED_FORMAT'] = args.output_filetype
    project_settings.overrides['FEED_URI'] = feedPath
    process = CrawlerProcess(project_settings)
    if args.shouldDownload == 'No':
        process.crawl(SearchEngineScrapy, searchquery=args.searchquery, filetype=args.filetype, pages=args.pages, searchengine=args.searchengine)
    else:
        process.crawl(SearchEngineScrapy, searchquery=args.searchquery, filetype=args.filetype, pages=args.pages, searchengine=args.searchengine, downloadfolder=args.downloadfolder)
    process.start()