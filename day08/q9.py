#Write a function that reads a JSON file and extracts specific information from it.

import json

def get_element(element, json_file):
    json_dict = json_file.get("user", {})
    for key, value in json_dict.items():
        if key == element:
            return value
    return None

def copy_file(file):
    with open(file, 'r') as data:
        content = json.load(data)
    return content

def main():
    json_file_name = "q9.json"
    json_file = copy_file(json_file_name)
    element = "first_name"
    result = get_element(element, json_file)
    print(result)

if __name__ == "__main__":
    main()
