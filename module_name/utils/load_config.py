import yaml
import json


def load_yaml(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)


def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def load_config(file_path):
    if file_path.endswith('.yaml'):
        return load_yaml(file_path)
    elif file_path.endswith('.json'):
        return load_json(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")

