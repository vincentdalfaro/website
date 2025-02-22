
from bs4 import BeautifulSoup
import json
import requests
from db_connect import client
from enable_log import logger


# API request for data 
logger.info("Requesting data from API")
URL = "https://api.rec.us/v1/locations?radius=1000000000&organizationSlug=san-francisco-rec-park"

try: 
    response = requests.get(URL)

except:
    logger.error("An error occured")
    
html_data = response.text


#Converting data into HTML format
soup = BeautifulSoup(html_data, 'html.parser')
formatted_html = soup.prettify()

formatted_html = json.loads(formatted_html)

# Connecting to our db (itstennistime_db) and storing data in collection (sf_tennis_courts)
try:
    db = client["itstennistime_db"]
    collection = db["sf_tennis_courts"]
    collection.drop()

    for park in formatted_html:
        user_result = collection.insert_one(park)

    logger.info("Successfully stored parks data in DB")

except Exception as e:
    print(f"Error: {e}")
    logger.error("An error occured storing parks data the DB")
