import os

from utils import load_properties_as_env, OPEN_AI_APIKEY

load_properties_as_env()

api_key = os.getenv(OPEN_AI_APIKEY)
print(">> "+api_key)