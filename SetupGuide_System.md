## Mac Setup Guide  to Install Web Crawler
  
Note: All `grey highlighted` lines are terminal commands. You can do this in a single shell window.

### Before Setting Up crawler  

**Step 1:**  
_pip_ is required for the crawler.  
To Install _pip_,  
use Command:  
`sudo easy_install pip`  
(Type `pip --version` to see if it is installed correctly)  
  
  
### Setting up crawler  
1. Copy SearchEngineScrapy folder from location provided to you to any directory (Example: ~/Documents/)  
2. `cd SearchEngineScrapy`    
5. `sudo pip install -r requirements.txt --ignore-installed`  (You need to re-run this command if this throws an error after accepting prompt to install xcode cmdline tools.)
  
  
### Running the Crawler  
1. Goto SearchEngineScrapy folder  (Example : `cd ~/Documents/SearchEngineScrapy/` : If it placed in Documents)     
  
_Run commands now to crawl the results:_  
Example (To crawl 5 pages of search results for PDFs with keyword 'Machine Learning' and store URLs in output_filename.csv):  
   
To use Bing Search Engine:  
`scrapy crawl SearchEngineScrapy -a searchQuery="Machine Learning" -a fileType="pdf" -a searchEngine="Bing" -a pages=5 -o output_filename_bing.csv`   

To use Google Search Engine:  
`scrapy crawl SearchEngineScrapy -a searchQuery="Machine Learning" -a fileType="pdf" -a searchEngine="Google" -a pages=5 -o output_filename_google.csv`   

(output_filename will contain URLs that are of filetype: pdf and query: 'Machine Learning')
  
### Parameters of the Crawler  
| Parameter       | Prefix | Description                                  | Options                       | Required | Default |
|-----------------|--------|----------------------------------------------|-------------------------------|----------|---------|
| searchQuery     | -a     | Search Query                                 | -                             | Y        | -       |
| fileType        | -a     | Filetype that you want to search for         | pdf/csv/zip/doc/docx/jpeg/png | Y        | -       |
| searchEngine    | -a     | Search Engine you want to use                | Google/Bing                   | N        | Bing    |
| pages           | -a     | Number of pages to crawl                     | -                             | N        | 3       |
| output_filename | -o     | name of output file where results are dumped | json/jsonl/csv/xml            | N        | -       |
  
  
### Downloading the crawled results   
Files are automatically downloaded and placed in downloads folder