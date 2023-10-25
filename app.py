# The CSVORM class is created to provide basic Object-Relational Mapping (ORM) operations
# for reading data from a CSV file.

class CSVORM:
    # The constructor takes a file_path as an argument, which should be the path to the
    # CSV file you want to work with.
    def __init__(self, file_path):
        self.file_path = file_path  # Store the file path for later use

    # The list_all method reads and returns all records from the CSV file as a list of dictionaries.
    def list_all(self):
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)  # Create a CSV DictReader object
            return [row for row in reader]  # Return all rows as a list of dictionaries

    # The get method takes an 'id' as an argument and searches for a record with that ID
    # in the CSV file. It returns the record as a dictionary if found, or None if not found.
    def get(self, id):
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)  # Create a CSV DictReader object
            for row in reader:  # Iterate through the rows in the CSV
                if row['ID'] == id:  # Check if the 'ID' field matches the provided 'id'
                    return row  # Return the matching record
        return None  # Return None if no matching record is found

    # The filter method takes a 'column_name' and a 'value' as arguments and filters the
    # records based on the specified column and value. It returns the filtered records
    # as a list of dictionaries.
    def filter(self, column_name, value):
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)  # Create a CSV DictReader object
            return [row for row in reader if row.get(column_name) == value]

# The following code block demonstrates the usage of the CSVORM class.
if __name__ == '__main__':
    # Create an instance of the CSVORM class, specifying the path to the CSV file.
    database = CSVORM('data/database.csv')

    # List all records
    print("List all records:")
    all_records = database.list_all()
    for record in all_records:
        print(record)

    # Get a specific record by ID
    print("\nGet a specific record:")
    specific_record = database.get('1')
    if specific_record:
        print(specific_record)
    else:
        print("Record not found")

    # Filter records based on a column and value
    print("\nFilter records:")
    filtered_records = database.filter('ColumnName', 'SomeValue')
    for record in filtered_records:
        print(record)
