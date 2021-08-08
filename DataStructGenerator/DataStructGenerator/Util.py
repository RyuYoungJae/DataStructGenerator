import os;
from nltk.tokenize import RegexpTokenizer

class Util(object):
    def DeleteFileIfExist(self, path):
         if os.path.isfile(path):
            os.remove(path)

    def CreateDirectoryIfNotExist(self, path):
        tokenizer = RegexpTokenizer(".*/")
        result = tokenizer.tokenize(path)
        dirPath ="".join(result)
      
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)