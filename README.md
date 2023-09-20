## Biocomputational Languages Test

Writing an example function in multiple languages to asses whether I should take Biocomputational Languages or Advanced Biocomputational Languages at Drexel School of Biomedical Engineering 

### Function Write Test

Write a function xls_columnaverage(file, columnname) that takes as input arguments: the name of
an Excel file and the name of a column of interest. Assume that the first row of the Excel file
contains the field names (describing what each column contains), and the remaining rows contain
numerical data. Your function should load the data contained in the Excel file and calculate the
average of the column whose name is contained in columnname. The column average should be returned
from the function. Your function should work when it is called with any Exccel file and column name,
assuming the Excel file satisfies the constraints described above.
To test your function, create two example Excel files called sample1.xlsx and sample2.xlsx. Add mock
patient information to these Excel files. Make sample2 columns be in different order than sample1.
Include columns representing name, age, height, and weight. Add several rows of example patients to
each of these files.
Test your function (in Matlab command window – or adapt these test case codes to your programming
language) with the following test cases:

- `xls_columnaverage('sample1.xlsx','age')`
- `xls_columnaverage('sample2.xlsx','weight')`

Double-check the answers from your function and make sure they match with what you get from manual
calculations of the data.

#### Example Data

Example Excel files `sample1.xlsx` and `sample2.xlsx` were randomly generated in R, see `write_function_test.Rmd`.

#### Example Code

- For `R`, see `write_function_test.Rmd`
- For `python`, see `write_function_test.py`
