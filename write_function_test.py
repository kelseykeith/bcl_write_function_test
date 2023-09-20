

def xls_columnaverage(file, columnname):
  from pandas import read_excel
  excelfile = read_excel(file)
  average = excelfile[columnname].mean()
  return average

xls_columnaverage('sample1.xlsx', 'age') # 53.6
xls_columnaverage('sample2.xlsx', 'weight') # 195.3
