#Credit to Gwen Rathgeber/Ben Mathis
import datetime 
import time
import requests
import json

subreddits = ['relationship_advice','AmItheAsshole']
kind = "submission"  # we want text posts

# Establish URL base
BASE_URL = f"https://api.pushshift.io/reddit/search/{kind}" # also known as the "API endpoint"

last_date = datetime.datetime.utcfromtimestamp(time.time())     #utc from timestamp 
posts = {}  #empty dictionary
for subreddit in subreddits:
    posts[subreddit] = []
    day = 2                       #start with the most recent post
    cumulative_posts = 0
   
    while cumulative_posts < 15000:                           #scrape 15,000 b/c minimum is 10,000 and some will be junk from what you scrape
        stem = f"{BASE_URL}?subreddit={subreddit}&size=100"   #part of query, #will scrape from 100 posts
        URL = f"{stem}&after={day}d"                           #will scrape from after the day we scrape it
        print("Querying from: " + URL)
        try:                                                  #we use try, except b/c scraping from the web, you'll get a lot of errors
            res = requests.get(URL)
            assert res.status_code == 200
            json = res.json()['data']
            df = pd.DataFrame(json)
            posts[subreddit].append(df)
            cumulative_posts += df.shape[0]
            final_date_pulled = datetime.datetime.utcfromtimestamp(df.iloc[-1, df.columns.get_loc('created_utc')])
            # increment = (last_date - final_date_pulled).days + 1
            # increment = increment if increment > 0 else 1
            day += 1
            # last_date = final_date_pulled
            print('successful')
        except:
            print(f'Scrape for {URL}, {day} failed')

        time.sleep(2)                    #this is a delay in between scrapes

print("Query complete!")

thoughts_frame = pd.concat(posts['relationship_advice'])
unpopular_frame = pd.concat(posts['AmItheAsshole'])

thoughts_frame.to_csv('./data/relationship_advice_initial_scrape.csv')
unpopular_frame.to_csv('./data/AmItheAsshole_initial_scrape.csv')