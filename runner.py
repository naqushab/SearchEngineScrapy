import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from SearchEngineScrapy.spiders.searchenginespider import SearchEngineScrapy

from gooey import Gooey, GooeyParser


@Gooey( program_name="Search Engine Scrapy")
def arg_parse():
    parser = GooeyParser(description='Crawl Search Engine Results and optionally download them')

    parser.add_argument(
        'searchquery',
        metavar='Search Query',
        help='Enter some search query',
        gooey_options={
            'validator': {
                'test': 'user_input != ""',
                'message': 'Enter some search query'
            }
        })
    parser.add_argument(
        'filetype',
        metavar='File Type',
        widget='Dropdown',
        choices=['pdf', 'csv', 'zip', 'doc', 'docx', 'jpeg', 'png'],
        help='Enter file type to search for',
        gooey_options={
            'validator': {
                'test': 'user_input != "Select Option"',
                'message': 'Choose a filetype from the list'
            }
        })
    parser.add_argument(
        'searchengine',
        metavar='Search Engine',
        widget='Dropdown',
        choices=['Bing', 'Google'],
        help='Search Engine to use',
        default='Bing',
        gooey_options={
            'validator': {
                'test': 'user_input != "Select Option"',
                'message': 'Choose a search engine from the list'
            }
        })
    parser.add_argument(
        'pages',
        metavar='Pages to Crawl',
        help='Enter number of pages to crawl',
        type=int,
        default=3,
        gooey_options={
            'validator': {
                'test': 'user_input != ""',
                'message': 'Enter page count > 0'
            }
        })
    parser.add_argument(
        'output_filename',
        metavar='Output Filename',
        help='Enter filename without extension',
        default='result',
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
        help='Enter output file type',
        default='csv',
        gooey_options={
            'validator': {
                'test': 'user_input != "Select Option"',
                'message': 'Choose a filetype from the list'
            }
        })
    parser.add_argument(
        'downloadfolder',
        metavar='Download Folder',
        widget='DirChooser',
        help='Enter where to save files (Optional)')
    
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = arg_parse()
    project_settings = get_project_settings()
    project_settings.overrides['FEED_FORMAT'] = args.output_filetype
    project_settings.overrides['FEED_URI'] = args.output_filename + '.' +  args.output_filetype
    process = CrawlerProcess(project_settings)
    if args.downloadfolder == "":
        process.crawl(SearchEngineScrapy, searchquery=args.searchquery, filetype=args.filetype, pages=args.pages, searchengine=args.searchengine)
    else:
        process.crawl(SearchEngineScrapy, searchquery=args.searchquery, filetype=args.filetype, pages=args.pages, searchengine=args.searchengine, downloadfolder=args.downloadfolder)
    process.start()