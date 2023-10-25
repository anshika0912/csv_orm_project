import csv

class CSVORM:
    def __init__(self, file_path):
        self.file_path = file_path

    def list_all(self):
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def get(self, id):
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ID'] == id:
                    return row
        return None

    def filter(self, column_name, value):
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return [row for row in reader if row.get(column_name) == value]

if __name__ == '__main__':
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
