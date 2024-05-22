from dotenv import load_dotenv
import os

def Load_Env_Vars():

    load_dotenv()
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    redirect_uri = os.getenv('REDIRECT_URI')

    return client_id, client_secret, redirect_uri
