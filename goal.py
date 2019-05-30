import requests
import signal
import sys
from bs4 import BeautifulSoup
from playsound import playsound

def signal_handler(signal, frame):
    print("Exiting...")
    sys.exit(0)
    
base_url = 'https://twitter.com'
def scrape_tweets(account):
    url = '{}/{}'.format(base_url, account)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    first_tweet = soup.find('p', attrs={'class': 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'})
    #print(first_tweet)
    return first_tweet

def isGoal(tweet):
    return(tweet.find('img', attrs={'src': 'https://abs.twimg.com/emoji/v2/72x72/1f6a8.png'}))
    #if(emoji):
        #print("True")
    #else:
        #print("False")

signal.signal(signal.SIGINT, signal_handler)
lastPage = scrape_tweets('nhlBruins')
while True:
    curPage = scrape_tweets('nhlBruins')
    if(curPage != lastPage):
        lastPage = curPage
        if(isGoal(curPage)):
            print("GOAL!")
            playsound('boston-bruins-goal-horn-2011-2012-mp3cut.mp3')
