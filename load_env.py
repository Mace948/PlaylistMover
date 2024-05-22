from dotenv import load_dotenv
import os

# Get Env Variables
def Load_Env_Vars():

    load_dotenv()
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')

    user_id = os.getenv('USER_ID')
    redirect_uri = os.getenv('REDIRECT_URI')

    deezer_user_id = os.getenv('DEEZER_USER_ID')

    return client_id, client_secret, user_id, redirect_uri, deezer_user_id
