import os
import json

SCHEMA_DATA_FILE = "schema_data.json"

def clear_screen():
    # Function to clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def load_schema_data():
    if os.path.exists(SCHEMA_DATA_FILE):
        with open(SCHEMA_DATA_FILE, 'r') as f:
            try:
                schema_data = json.load(f)
                # Convert schema data from list of lists to list of tuples
                schema_data = {filename: [tuple(entry) for entry in schema] for filename, schema in schema_data.items()}
            except json.JSONDecodeError:
                schema_data = {}
    else:
        schema_data = {}
    
    return schema_data

def save_schema_data(schema_data):
    # Convert schema data from list of tuples to list of lists before saving
    schema_data = {filename: [list(entry) for entry in schema] for filename, schema in schema_data.items()}
    with open(SCHEMA_DATA_FILE, 'w') as f:
        json.dump(schema_data, f, indent=2)

def create_json_file():
    clear_screen()
    filename = input("Enter the name for the JSON file (without extension): ")
    filename += ".json"
    
    if os.path.exists(filename):
        print(f"A file with the name '{filename}' already exists.")
        return
    
    schema = []
    while True:
        field_name = input("Enter field name (leave blank to finish schema creation): ").strip()
        if not field_name:
            break
        
        print("Choose field type:")
        print("1. Integer")
        print("2. Text")
        field_type = input("Enter field type (1 for int, 2 for text): ").strip()
        if field_type not in ['1', '2']:
            print("Invalid choice. Use '1' for int or '2' for text.")
            continue
        
        if field_type == '1':
            field_type = 'int'
        elif field_type == '2':
            field_type = 'text'
        
        schema.append((field_name, field_type))
    
    with open(filename, 'w') as f:
        json.dump([], f)  # initialize empty list as data
        
    schema_data = load_schema_data()
    schema_data[filename] = schema
    save_schema_data(schema_data)
    
    print(f"Created schema for '{filename}':")
    print(schema)

def add_data_to_json():
    clear_screen()
    files = [f for f in os.listdir() if f.endswith('.json')]
    if not files:
        print("No JSON files found in the current directory.")
        return
    
    print("Existing JSON files:")
    for i, filename in enumerate(files, 1):
        print(f"{i}. {filename}")
    
    selection = input("Select the file to add data (enter number): ")
    try:
        selection = int(selection) - 1
        filename = files[selection]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return
    
    schema_data = load_schema_data()
    if filename not in schema_data:
        print(f"No schema data found for '{filename}'. Attempting to infer schema from existing data.")
        
        with open(filename, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"Error: '{filename}' is not a valid JSON file.")
                return
            
            if not data:
                print(f"Error: '{filename}' has no existing data. Cannot infer schema.")
                return
            
            # Assume schema from the first item in the data
            first_item = data[0]
            schema = [(key, 'int' if isinstance(value, int) else 'text') for key, value in first_item.items()]
            
            schema_data[filename] = schema
            save_schema_data(schema_data)
            
            print(f"Inferred schema for '{filename}':")
            print(schema)
    else:
        schema = schema_data[filename]
        print(f"Schema for '{filename}':")
        print(schema)
        
        # Now allow adding data
        print(f"Adding data to '{filename}'...")
        new_data = {}
        for field_name, field_type in schema:
            value = input(f"Enter value for '{field_name}' ({field_type}): ").strip()
            if field_type == 'int':
                try:
                    value = int(value)
                except ValueError:
                    print(f"Invalid value '{value}' for '{field_name}'. Expected an integer.")
                    return
            # You can add more type checking if needed
            
            new_data[field_name] = value
        
        with open(filename, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"Error: '{filename}' is not a valid JSON file.")
                return
        
        data.append(new_data)
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print("Data added successfully.")

def main():
    while True:
        choice = input("Enter for menu")
        clear_screen()
        print("Options:")
        print("1. Create new JSON file schema")
        print("2. Add data to existing JSON file")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            create_json_file()
        elif choice == '2':
            add_data_to_json()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
