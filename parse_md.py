import re

def extract_inline_fields(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match lines with the format Key:: Value
    fields = re.findall(r'^\s*([\w\s]+)::\s*(.+?)\s*$', content, re.MULTILINE)

    # Convert to dictionary
    field_dict = {key.strip(): value.strip() for key, value in fields}
    return field_dict

# Example usage
file_path = "your_note.md"
fields = extract_inline_fields(file_path)

print(fields)
