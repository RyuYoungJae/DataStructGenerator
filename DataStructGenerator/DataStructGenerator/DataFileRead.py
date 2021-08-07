import openpyxl as xl
import glob2

class DataFileRead(object):
    def Read(self, path):
        result = {}
        xlFiles = glob2.glob(path)
        for file in xlFiles:
            wb = xl.load_workbook(file)
            for sheetName in wb.sheetnames:
                if sheetName != "Define":
                    continue

                cells = []
                sheet = wb[sheetName]
                for row in sheet.iter_rows(min_row=1):
                    for cell in row:
                        cells.append(cell.value)
                
                result[sheetName] = cells
            wb.close()
        return result


