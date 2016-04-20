from twython import Twython, TwythonError
import json
import requests

CONSUMER_KEY = '3atqlB1OilzcWPga7f6EIv3Cf'
CONSUMER_SECRET = 'HiHfmC1Rs4pL96kXto4lGcwPXDDjl86olRC3zP7AhBBqP2efAD'
ACCESS_TOKEN = '722879150684381186-EQBYL8wY2yjpSavegm3CYIsNvBcP0C5'
ACCESS_TOKEN_SECRET = 'rtt4GSZGCjBWPqNzDcmnanBbUpz8s6XCHjFwVdi0JmGSq'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

r= request.get()
json = r.json

try:
    twitter.update_status(status='Wow! that was easy!')
except TwythonError as e:
    print e

# read from csv
