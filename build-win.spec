import gooey
gooey_root = os.path.dirname(gooey.__file__)
gooey_languages = Tree(os.path.join(gooey_root, 'languages'), prefix = 'gooey/languages')
gooey_images = Tree(os.path.join(gooey_root, 'images'), prefix = 'gooey/images')
a = Analysis(scripts=['runner.py'],
             pathex=['C:\\Users\\neyazee\\Documents\\GitHub\\SearchEngineScrapy\\venv\\Scripts', 'C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\ucrt\\DLLs\\x86'],
             hiddenimports=['SearchEngineScrapy.spiders.searchenginespider'],
             hookspath=['.\\hooks\\'],
             runtime_hooks=[],
             excludes=[],
             datas=[('.\\SearchEngineScrapy\\spiders\\','.\\spiders\\'), ('.\\SearchEngineScrapy\\utils\\','.\\utils\\'),
                    ('.\\SearchEngineScrapy\\settings.py','.\\settings.py'), ('.\\SearchEngineScrapy\\items.py','.\\items.py'),
                    ('.\\SearchEngineScrapy\\middlewares.py','.\\middlewares.py'), ('.\\SearchEngineScrapy\\pipelines.py','.\\pipelines.py'),
                    ('scrapy.cfg','.')
                   ]
             )
pyz = PYZ(a.pure, a.zipped_data)

options = [('u', None, 'OPTION'), ('v', None, 'OPTION'), ('w', None, 'OPTION')]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          options,
          gooey_languages, # Add them in to collected files
          gooey_images, # Same here.
          name='SearchEngineScrapy',
          debug=False,
          strip=None,
          upx=True,
          console=False,
          windowed=True)