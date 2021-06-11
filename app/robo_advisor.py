# this is the "app/robo_advisor.py" file

import os
import dotenv 
import load_dotenv
import requests

load_dotenv()

#read env variabkes
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

#make a request

symbol = "MSFT"
request_url - "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"

response = requests.get(request_url)

print(type(response))
print(response.text)