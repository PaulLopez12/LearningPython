import os

from dotenv import load_dotenv
from pymongo import MongoClient

#Carga las variables de entorno del fichero .env.local (solo local)
load_dotenv(".env.local")

#Conexion a base de datos en la nube
#Define MONGODB_URL como variable de entorno en Vercel
db_client = MongoClient(
    os.environ["MONGODB_URL"]).test