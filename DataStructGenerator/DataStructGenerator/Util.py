import os;

class Util(object):
    def DeleteFileIfExist(self, path):
         if os.path.isfile(path):
            os.remove(path)

    def CreateDirectoryIfNotExist(self, path):
        dirPath = os.path.dirname(path)
      
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)

    def TypeParsing(self, type):
        if type == "INT": return "int32_t"
        elif type == "STRING": return "std::string"
        elif type == "FLOAT": return "float"
        else: return "none"

    def GetFileName(self, path):
        return os.path.splitext(os.path.basename(path))