import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker #No entendí porque no salía en el VE
import requests
import json #este no necesita se descargado en el VE porque viene por defecto en python 
from datetime import datetime
import datetime
import sqlite3 #este no necesita se descargado en el VE porque viene por defecto en python 


DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID = "dannarbuitrago" # your Spotify username 
TOKEN = "BQAB5cILTvj0aaOddA7yptTkX-vfwcnxGc8Ev9akAlo4RclEUWR6Lq4JUFvzvmMtO55wx8LfdKYBCNNbjnVGI0d2haSsrSzPQs5KRpbQQOyjUrEQU_N4JcobLVkwY4mbF7j_ctt233V-DvERmEbXBG7rOzHNHhJM-LWeyDcJQldNAhWzg9GSH5TmPeVKeQkuhjp6Mnr38FpMKvotc2Nx48nBTZMZy8ATXv9YIOs_zaAh_Mv8odV7L9AjLo2w0mRpRKs6n9-26w" # your Spotify API token

if __name__ == "__main__":

    # Extract part of the ETL process
 
    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }
    
    # Convert time to Unix timestamp in miliseconds      
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1) # we want to see this daily 
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000
    
    # Download all songs you've listened to "after yesterday", which means in the last 24 hours      
    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers)

    data = r.json()
    
    print(data)

  