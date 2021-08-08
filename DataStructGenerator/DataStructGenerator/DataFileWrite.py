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
      self.__WriteInclude(handle)

      for sheet, factors in datas.items():
         handle.write("struct" + " " + sheet + "\n")
         handle.write("{ \n")
         for varName, type in factors.items():
            util = Util.Util()
            resultType = util.TypeParsing(type)
            if resultType == "none": 
                cotinue
            handle.write("\t" + resultType + "\t" + varName + ";\n")

         handle.write("} \n\n")

      handle.close()

   def __WriteInclude(self, handle):
      handle.write("#include <stdint.h> \n")
      handle.write("#include <string> \n")
     