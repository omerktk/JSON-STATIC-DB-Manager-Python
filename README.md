# JSON DB Manager in Python

This Python script enables you to manage static JSON files as a custom database system. It allows you to define JSON schemas, add data to existing JSON files according to these schemas, and maintain metadata for each schema.

## Features:
- **Schema Definition**: Define JSON file schemas interactively.
- **Data Management**: Add data to existing JSON files based on predefined schemas.
- **Metadata Storage**: Store and manage schema metadata in `schema_data.json`.
- **User-friendly Interface**: Simple command-line interface for ease of use.

## Files:
- `app.py`: Main Python script containing functionalities to create schemas and add data.
- `products.json`, `users.json`: Example JSON files for storing data.
- `schema_data.json`: Metadata file storing JSON file schemas.

## Usage:
1. **Create Schema**: Run the script and choose option 1 to define a new JSON file schema.
2. **Add Data**: Choose option 2 to add data to an existing JSON file based on its schema.
3. **Exit**: Option 3 exits the program.

## Getting Started:
To get started, clone the repository and run `app.py` in your Python environment.

```bash
python app.py
