import os
import Util

class DataFileWrite(object):
   def GeneratorFile(self, datas, path):
       self.__Prepare(path)
       self.__WriteFile(datas, path)

   def __Prepare(self, path):
       util = Util.Util()
       util.CreateDirectoryIfNotExist(path)
       util.DeleteFileIfExist(path)

   def __WriteFile(self, datas, path):
       handle = open(path, "w")
       handle.writelines("#include \"stdint.h\"")
       