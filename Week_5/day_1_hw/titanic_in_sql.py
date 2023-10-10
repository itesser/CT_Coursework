from dotenv import load_dotenv
from os import getenv
import psycopg2

load_dotenv()

user = getenv('USER')
password = getenv('PASSWORD')
server = getenv('SERVER')

