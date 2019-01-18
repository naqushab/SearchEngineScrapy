from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# This collects all dynamically imported scrapy modules and data files.
hiddenimports = (collect_submodules('scrapy') +
                 collect_submodules('scrapy.pipelines') +
                 collect_submodules('scrapy.extensions') +
                 collect_submodules('scrapy.utils') +
                 collect_submodules('SearchEngineScrapy')
)
datas = collect_data_files('scrapy')