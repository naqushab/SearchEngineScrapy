import re
import errno    
import os

class Utilities:

    def __init__(self):
        pass
    
    def is_filetype(self, fileType, urlInfo):
        fileType_dict = {
            'pdf': 'application/pdf',
            'csv': 'text/csv',
            'zip': 'application/zip',
            'doc': 'application/msword',
            'docx': 'application/msword',
            'jpeg': 'image/jpeg',
            'png': 'image/png'
        }
        if urlInfo.headers['content-type'] == fileType_dict.get(fileType, "None"):
            return True
        else:
            return False

    def get_filename(self, fileType, url, urlInfo):
        fname = ''
        if "Content-Disposition" in urlInfo.headers.keys():
            fname = re.findall("filename=(.+)", urlInfo.headers["Content-Disposition"])[0]
        else:
            fname = url.split("/")[-1]
        fname = self.clean_filename(fname, fileType)
        return fname

    def clean_filename(self, fname, fileType, stripSpaces=False):
        fname = re.sub(r'[^.,a-zA-Z0-9]+', ' ', fname)
        if stripSpaces:
            re.sub(r'\s+', '', fname)
        fname = fname.strip()
        if fname.find(".") == -1:
            fname = "{0}.{1}".format(fname, fileType)
        else:
            fname = ''.join(fname.split('.')[0:-1])
            fname = "{0}.{1}".format(fname, fileType)
        return fname

    def create_folder_structure(self, path):
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise ("Directory cannot be made due to OS error, select another path")
        return path