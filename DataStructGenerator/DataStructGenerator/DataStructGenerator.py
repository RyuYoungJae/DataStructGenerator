import DataFileRead
import DataFileWrite

path = "../../Data/*.xlsx"
createPath = "../../Code/DataStruct.h"

reader = DataFileRead.DataFileRead()
result = reader.Read(path)

writer = DataFileWrite.DataFileWrite()
writer.GeneratorFile(result, createPath)