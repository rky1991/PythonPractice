#Method 1: Using pandas (Recommended for Large Files)python
import pandas as pd

# Read CSV file
df = pd.read_csv("C:\PythonWorkSpace\PythonBasicsLearnings\ExcelOperations\Files\Sdata.csv")

# Display the first 5 rows
print(df.head())
print("Hello")