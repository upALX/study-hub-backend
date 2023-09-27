from pathlib import Path
from os import path, environ
import sys


root = Path.cwd()
sys.path.append(str(root) + "/src")
if not environ.get("APP_ENV") or environ.get("APP_ENV") == "local":
    from dotenv import load_dotenv

    dot_env_path = path.join(str(root), "local.env")
    load_dotenv(dot_env_path)