import os
import json

def save_to_json(data, query):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{query}.json")
 
    with open(file_path, 'w') as json_file:
        json.dump([product.to_dict() for product in data], json_file, indent=4)
    print(f"Data for query '{query}' saved to {file_path}")
