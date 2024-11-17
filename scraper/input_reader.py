import json

def read_queries(file_path="user_queries.json"):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
        return []