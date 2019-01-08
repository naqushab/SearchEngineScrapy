## Mac Setup Guide  
  
### Before Setting Up crawler  

**Step 1:**  
You need to have python installation on your mac.  
Type `which python` to see if you have Python 2.7 installed.  
  
  
If you don't have Python 2.7, install Homebrew to install it. _Otherwise, skip this step to install pip and virtualenv._
  
Type command:  
`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`  
`export PATH="/usr/local/bin:/usr/local/sbin:$PATH"`  
`brew install python@2`  
`export PATH="/usr/local/opt/python@2/libexec/bin:$PATH"`  
  
**Step 2:**  
`pip` and `virtualenv` are two more things required for the crawler.  
To Install `pip`,  
use Command:  
`sudo easy_install pip` (Type `pip --version` to see if it is installed correctly)  
To Install `virtualenv`,  
use Command:  
`pip install virtualenv`  
  
  
### Setting up crawler  
1. Copy SearchEngineScrapy folder to any directory (Example: ~/Documents/)  
2. `cd SearchEngineScrapy`   
3. `virtualenv -p python venv`  
4. `source venv/bin/activate`  
5. `pip install -r requirements.txt`  
  
  
### Running the Crawler  
1. Goto SearchEngineScrapy folder   
2. Example : `cd ~/Documents/SearchEngineScrapy/` (If it placed in Documents)  
3. `source venv/bin/activate` (Activate virtualenv)  
4. `cd SearchEngineScrapy`  
  
_Run commands now to crawl the results:_  
Example (To crawl 5 pages of Google search results for PDFs with keyword Adobe and store URLs in output_filename.csv):  
*(venv) ~/Documents/SearchEngineScrapy/SearchEngineScrapy*> `scrapy crawl SearchEngineScrapy -a searchQuery="Adobe" -a fileType="pdf" -a searchEngine="Google" -a pages=5 -o output_filename.csv`   
  
### Parameters of the Crawler  
| Parameter       | Prefix | Description                                  | Options                       | Required | Default |
|-----------------|--------|----------------------------------------------|-------------------------------|----------|---------|
| searchQuery     | -a     | Search Query                                 | -                             | Y        | -       |
| fileType        | -a     | Filetype that you want to search for         | pdf/csv/zip/doc/docx/jpeg/png | Y        | -       |
| searchEngine    | -a     | Search Engine you want to use                | Google/Bing                   | N        | Bing    |
| pages           | -a     | Number of pages to crawl                     | -                             | N        | 3       |
| output_filename | -o     | name of output file where results are dumped | json/jsonl/csv/xml            | N        | -       |