import os
from dotenv import load_dotenv

environment = os.getenv('ENVIRONMENT')

if environment != "local":
    load_dotenv(dotenv_path='.env', override=True)

class Config:
    ENVIRONMENT = environment
    APP_NAME=os.getenv('APP_NAME')