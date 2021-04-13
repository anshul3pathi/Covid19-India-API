import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / ".env" 
load_dotenv()
print(os.getenv('CHROME_DRIVER_PATH'))
print(os.getenv("DEBUG"))