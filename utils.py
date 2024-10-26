import os

def load_properties_as_env(file_rel_path="/.venv/local.properties"):
    filepath = os.getcwd() + file_rel_path
    if os.path.exists(filepath):
        with open(filepath) as file:
            for line in file:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    os.environ[key.strip()] = value.strip()  # Set as environment variable

OPEN_AI_APIKEY = "open_ai_key2"