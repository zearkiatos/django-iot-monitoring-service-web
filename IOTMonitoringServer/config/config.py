import os
from dotenv import load_dotenv

environment = os.getenv('ENVIRONMENT')

if environment != "local":
    load_dotenv(dotenv_path='.env', override=True)

class Config:
    ENVIRONMENT = environment
    APP_NAME=os.getenv('APP_NAME')
    ALLOWED_HOSTS=os.getenv('ALLOWED_HOSTS')
    DATABASE_HOST=os.getenv('DATABASE_HOST')
    DATABASE_USER=os.getenv('DATABASE_USER')
    DATABASE_PASSWORD=os.getenv('DATABASE_PASSWORD')
    DATABASE_PORT=os.getenv('DATABASE_PORT')
    DATABASE_NAME=os.getenv('DATABASE_NAME')
    MQTT_HOST=os.getenv('MQTT_HOST')
    MQTT_USER=os.getenv('MQTT_USER')
    MQTT_PASSWORD=os.getenv('MQTT_PASSWORD')
    MQTT_USER_PUB=os.getenv('MQTT_USER_PUB')
    MQTT_PASSWORD_PUB=os.getenv('MQTT_PASSWORD_PUB')