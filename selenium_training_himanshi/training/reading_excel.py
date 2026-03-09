
import xlrd

xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True

path = r'C:\Users\KIIT\Downloads\selenium_training\selenium_training_himanshi\files\Book1.xlsx'

## open the excel
workbook = xlrd.open_workbook(path)
# print(workbook)             ## book object

## open the worksheet
worksheet = workbook.sheet_by_name("Sheet1")
# print(worksheet)            ## sheet object

## convert the sheet object to the generator object
rows = worksheet.get_rows()
# print(rows)

# for ele in rows:
#     print(ele)

# for ele in rows:
#     print(ele[0], ele[1], ele[2])

for ele in rows:
    print(ele[0].value, ele[1].value, ele[2].value)
































































