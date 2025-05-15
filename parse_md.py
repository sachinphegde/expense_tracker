import re


def extract_inline_fields(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Match lines with the format Key:: Value
        fields = re.findall(r'^\s*([\w\s]+)::\s*(.+?)\s*$', content, re.MULTILINE)

        # Convert to dictionary
        field_dict = {key.strip(): value.strip() for key, value in fields}
        return field_dict
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except IOError as e:
        print(f"IO error opening file: {e}")
