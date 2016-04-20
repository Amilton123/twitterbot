from twython import Twython
import csv

APP_KEY = 'uqdFqqqnBq4ruOaGR1e2P2M9D'
APP_SECRET = 'LpIvtuF9Gjb3EwMObQ22VOUVgj1HiZi7n5caVeZ3wJ98hDSqOQ'
OAUTH_TOKEN = '722556363721818113-jGlE6zQLKMAn4DJqtz6MOyC7CCXODNB'
OAUTH_TOKEN_SECRET = 'vAnhXdWepDcB2XHQYjzViarCMbXFM0pqPSPqfQqgk8Kpq'

t = Twython(app_key=APP_KEY, app_secret=APP_SECRET, oauth_token=OAUTH_TOKEN, oauth_token_secret=OAUTH_TOKEN_SECRET)

search=t.search(q='propublica', count="100")
tweets= search['statuses']

with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)

#Open the CSV file. 'data.csv' can be renamed to whatever you would like. This is the filename it will save under.

    a.writerow(('Search Term', 'Tweet Text', 'URL'))

#At the top of the CSV file, we want to add in a row with columns labeled 'Search Term' and 'Tweet Text'.

    for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[['propublica', result['text'].encode('utf-8'), url]]
        a.writerows((text))
