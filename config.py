# Import libraries
import configparser

# Creating config object
config = configparser.ConfigParser()
config.read('config.ini')

class FlaskConfig:
    DEFAULT_HOST = config['FLASK']['DEFAULT_HOST']
    DEFAULT_PORT = config['FLASK']['DEFAULT_PORT']
