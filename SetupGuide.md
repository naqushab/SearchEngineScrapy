## Mac Setup Guide  
  
### Before Setting Up crawler  
You need to have python installation on your mac.  
Type `which python` to see if you have Python 2.7 installed.  
  
  
If you don't have Python 2.7, install Homebrew to install it. Otherwise, skip this step.  
Type command:  
`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`  
`export PATH="/usr/local/bin:/usr/local/sbin:$PATH"`  
`brew install python@2`  
`export PATH="/usr/local/opt/python@2/libexec/bin:$PATH"`  
  
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
  
Run commands now to crawl the results:  
Example:  
*(venv) ~/Documents/SearchEngineScrapy/SearchEngineScrapy*> `scrapy crawl SearchEngineScrapy -a searchQuery="Adobe" -a fileType="pdf" -a searchEngine="Google" -a pages=5 -o output_filename.csv`   
  
### Parameters of the Crawler  
Prefix : `-a`  
searchQuery="<your search query>" [Required Parameter]   
fileType="<filetype you want to search for>" [Options: pdf/csv/zip/doc/docx/jpeg/png] [Required Parameter]  
searchEngine="<your search engine>" [Options: Google/Bing(Default)] [Optional Parameter]   
pages=<number of pages to crawl> [Default: 3] [Optional Parameter]  
  
Prefix : `-o`  
<filename> [Output the results to a file] [Options: json/jsonl/csv/xml] [Optional Parameter]  