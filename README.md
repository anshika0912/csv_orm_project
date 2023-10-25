# CSVORM - CSV Object-Relational Mapping

CSVORM is a simple Python class that provides object-relational mapping (ORM) functionality for working with CSV data. It allows you to perform basic operations like listing all records, retrieving specific records by ID, and filtering records based on column values in a CSV file.

## Usage

1. **Installation**

   You can use the `CSVORM` class by simply including it in your Python project. There's no need to install any external packages.

2. **Initializing CSVORM**

   Create an instance of the `CSVORM` class, providing the path to your CSV file as an argument when you initialize the class.

   ```python
   database = CSVORM('data/database.csv')
   ```

3. **List All Records**

   To list all records in the CSV file:

   ```python
   all_records = database.list_all()
   for record in all_records:
       print(record)
   ```

4. **Get a Specific Record by ID**

   To retrieve a specific record by its ID:

   ```python
   specific_record = database.get('1')
   if specific_record:
       print(specific_record)
   else:
       print("Record not found")
   ```

5. **Filter Records**

   To filter records based on a column and a value:

   ```python
   filtered_records = database.filter('ColumnName', 'SomeValue')
   for record in filtered_records:
       print(record)
   ```

6. **Customization**

   - You can customize the `CSVORM` class to match your specific CSV file structure.
   - Modify the file path, field names, and data types according to your CSV file's schema.

## Sample CSV Data

Here's an example of the CSV data format used in the code:

```
ID  Name    Age Occupation
1   Rajesh  28  Engineer
2   Priya   24  Doctor
3   Anjali  32  Teacher
4   Sanjay  35  Designer
5   Amit    30  Manager
```
