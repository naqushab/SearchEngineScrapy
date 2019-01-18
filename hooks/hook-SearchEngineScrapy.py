from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# This hooks the scrapy project 'SearchEngineScrapy' to import all submodules, change name to match scrapy project
hiddenimports = (collect_submodules('SearchEngineScrapy'))