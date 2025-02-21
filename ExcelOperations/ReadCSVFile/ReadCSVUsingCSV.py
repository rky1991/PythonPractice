import csv

# Open and read CSV file
with open("C:\PythonWorkSpace\PythonBasicsLearnings\ExcelOperations\Files\Sdata.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list


print("************************************************")

# Read as dictionary ---->>>
with open("C:\PythonWorkSpace\PythonBasicsLearnings\ExcelOperations\Files\Sdata.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"])  # Access columns by name