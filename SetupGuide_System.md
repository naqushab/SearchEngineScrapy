## Mac Setup Guide to Install Web Crawler
  
Note: All `grey highlighted` lines are terminal commands. You can do this in a single shell window.

### Before Setting Up crawler  

**Step 1:**  
_pip_ is required for the crawler.  
To Install _pip_,  
use Command:  
`sudo easy_install pip`  (Type `pip --version` to see if it is installed correctly)  
  
  
### Setting up crawler  
1. Copy SearchEngineScrapy folder from location provided to you to any directory (Example: ~/Documents/)  
2. `cd SearchEngineScrapy`    
5. `sudo pip install -r requirements.txt --ignore-installed`  (You need to re-run this command if this throws an error after accepting prompt to install xcode cmdline tools.)
  
  
### Running the Crawler  
1. Goto SearchEngineScrapy folder  (Example : `cd ~/Documents/SearchEngineScrapy/` : If it placed in Documents)     
  
_Run commands now to crawl the results:_  
Example (To crawl 5 pages of search results for PDFs with keyword 'Machine Learning', store URLs in output_filename.csv and download the files in the downloadfolder mentioned):  
   
To use Bing Search Engine:  
`scrapy crawl SearchEngineScrapy -a searchquery="Machine Learning" -a filetype="pdf" -a searchengine="bing" -a pages=5 -a downloadfolder="/Users/neyazee/Documents/SearchEngineScrapy/downloads/" -o output_filename.csv`    

(output_filename will contain URLs that are of filetype: pdf and query: 'Machine Learning' and all the files are downloaded to /Users/neyazee/Documents/SearchEngineScrapy/downloads/.)
  
### Parameters of the Crawler  
| Parameter       | Prefix  | Description                                  | Options                       | Required | Default |
|-----------------|--------|----------------------------------------------|-------------------------------|----------|---------|
| searchquery     | -a     | Search Query                                 | -                             | Y        | -       |
| filetype         | -a     | filetype that you want to search for         | pdf/csv/zip/doc/docx/jpeg/png | Y        | -       |
| searchengine    | -a     | Search Engine you want to use                | Bing                          | N        | Bing    |
| pages           | -a     | Number of pages to crawl                     | -                             | N        | 3       |
| downloadfolder  | -a     | Path to the downloads folder *_(If not specified, files will not be downloaded)_*  | -                             | N        | -       |
| output_filename  | -o     | name of output file where results are dumped  | json/jsonl/csv/xml            | N        | -       |
  
  
### Downloading the crawled results   
Files are automatically downloaded and placed in _downloadfolder_ specified. (Uses system curl to achieve this.)  
if _downloadfolder_ parameter is not specified, the files will not get downloaded and only the URLs are crawled.