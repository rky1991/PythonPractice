#Method 1: Using pandas (Recommended for Large Files)python
import pandas as pd

# Read an Excel file
df = pd.read_excel("C:\PythonWorkSpace\PythonBasicsLearnings\ExcelOperations\Files\Studentdata.xlsx")


# Display the first 5 rows
print(df.head())