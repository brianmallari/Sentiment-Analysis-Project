from textblob import TextBlob
import csv
import tweepy
import unidecode

# from datetime import date
# import datetime
from datetime import datetime
# import time
from dateutil.tz import * 

# AUTHENTICATION (OAuth)
# f = open('auth.k','r')
f = open('my_own_auth.k','r')
ak = f.readlines()
f.close()
auth1 = tweepy.auth.OAuthHandler(ak[0].replace("\n",""), ak[1].replace("\n",""))
auth1.set_access_token(ak[2].replace("\n",""), ak[3].replace("\n",""))
api = tweepy.API(auth1)

# Tweeter search with keyword

# Twitter serach #1
# target_num = 50
# query = "olympics"
target_num = 200
query = "PlayStation 5"

# csvFile = open('results_olympics.csv','w')
# modification to the open() function
# (as per https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters)
# todaysDate = date.today()
# print(todaysDate)
currentDateAndTime = datetime.now()
# print(currentDateAndTime)
reformatedCurrentDateAndTime = currentDateAndTime.strftime("%Y-%m-%d_%H,%M,%S")
# print(reformatedCurrentDateAndTime)
# UTC_DateAndTime = datetime.utcnow()
# UTC_DateAndTime = datetime.utcnow(timezone.utc)
# print(UTC_DateAndTime)
# currentTimezone = time.tzname
# currentTimezone = datetime.tzname()
# currentTimezone = datetime.tzinfo
currentTimezone = datetime.now(tzlocal()).tzname()
# print(currentTimezone)
# abbreviatedCurrentTimezone = datetime(datetime.today(),tzinfo=tz).tzname()
# abbreviatedCurrentTimezone = datetime.tzname()
# abbreviatedCurrentTimezone = tzwinlocal()
# print(abbreviatedCurrentTimezone)
currentTimezoneAsList = currentTimezone.split(" ")
# print(currentTimezoneAsList)
reconstructedCurrentTimeZone = "".join(currentTimezoneAsList)
# print(reconstructedCurrentTimeZone)

resultsFilePrefix = "results_"
# baseResultsFileName = "results_olympics" 
baseResultsFileName = resultsFilePrefix + query
# print(baseResultsFileName)
newResultsFileName = baseResultsFileName + "_" + reformatedCurrentDateAndTime + "_" + reconstructedCurrentTimeZone
# print(newResultsFileName)
fileExtension = '.csv'
newResultsFileNameWithExtension = newResultsFileName + fileExtension
# print(newResultsFileNameWithExtension)

# csvFile = open(baseResultsFileName,'w', encoding = "utf-8")
csvFile = open(newResultsFileNameWithExtension,'w', encoding = "utf-8")
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["username","author id","created", "text", "retwc", "hashtag", "followers", "friends","polarity","subjectivity"])
counter = 0

for tweet in tweepy.Cursor(api.search, q = query, lang = "en", result_type = "popular", count = target_num).items():
    created = tweet.created_at
    text = tweet.text
    text = unidecode.unidecode(text) 
    retwc = tweet.retweet_count
    try:
        hashtag = tweet.entities[u'hashtags'][0][u'text'] #hashtags used
    except:
        hashtag = "None"
    username  = tweet.author.name            #author/user name
    authorid  = tweet.author.id              #author/user ID#
    followers = tweet.author.followers_count #number of author/user followers (inlink)
    friends = tweet.author.friends_count     #number of author/user friends (outlink)

    text_blob = TextBlob(text)
    polarity = text_blob.polarity
    subjectivity = text_blob.subjectivity
    csvWriter.writerow([username, authorid, created, text, retwc, hashtag, followers, friends, polarity, subjectivity])

    counter = counter + 1
    if (counter == target_num):
        break

csvFile.close()

# End of Twitter search #1

# Twitter serach #2
# target_num = 50
# query = "olympics"
target_num = 200
query = "Xbox Series X"

# csvFile = open('results_olympics.csv','w')
# modification to the open() function
# (as per https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters)
# todaysDate = date.today()
# print(todaysDate)
currentDateAndTime = datetime.now()
# print(currentDateAndTime)
reformatedCurrentDateAndTime = currentDateAndTime.strftime("%Y-%m-%d_%H,%M,%S")
# print(reformatedCurrentDateAndTime)
# UTC_DateAndTime = datetime.utcnow()
# UTC_DateAndTime = datetime.utcnow(timezone.utc)
# print(UTC_DateAndTime)
# currentTimezone = time.tzname
# currentTimezone = datetime.tzname()
# currentTimezone = datetime.tzinfo
currentTimezone = datetime.now(tzlocal()).tzname()
# print(currentTimezone)
# abbreviatedCurrentTimezone = datetime(datetime.today(),tzinfo=tz).tzname()
# abbreviatedCurrentTimezone = datetime.tzname()
# abbreviatedCurrentTimezone = tzwinlocal()
# print(abbreviatedCurrentTimezone)
currentTimezoneAsList = currentTimezone.split(" ")
# print(currentTimezoneAsList)
reconstructedCurrentTimeZone = "".join(currentTimezoneAsList)
# print(reconstructedCurrentTimeZone)

resultsFilePrefix = "results_"
# baseResultsFileName = "results_olympics" 
baseResultsFileName = resultsFilePrefix + query
# print(baseResultsFileName)
newResultsFileName = baseResultsFileName + "_" + reformatedCurrentDateAndTime + "_" + reconstructedCurrentTimeZone
# print(newResultsFileName)
fileExtension = '.csv'
newResultsFileNameWithExtension = newResultsFileName + fileExtension
# print(newResultsFileNameWithExtension)

# csvFile = open(baseResultsFileName,'w', encoding = "utf-8")
csvFile = open(newResultsFileNameWithExtension,'w', encoding = "utf-8")
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["username","author id","created", "text", "retwc", "hashtag", "followers", "friends","polarity","subjectivity"])
counter = 0

for tweet in tweepy.Cursor(api.search, q = query, lang = "en", result_type = "popular", count = target_num).items():
    created = tweet.created_at
    text = tweet.text
    text = unidecode.unidecode(text) 
    retwc = tweet.retweet_count
    try:
        hashtag = tweet.entities[u'hashtags'][0][u'text'] #hashtags used
    except:
        hashtag = "None"
    username  = tweet.author.name            #author/user name
    authorid  = tweet.author.id              #author/user ID#
    followers = tweet.author.followers_count #number of author/user followers (inlink)
    friends = tweet.author.friends_count     #number of author/user friends (outlink)

    text_blob = TextBlob(text)
    polarity = text_blob.polarity
    subjectivity = text_blob.subjectivity
    csvWriter.writerow([username, authorid, created, text, retwc, hashtag, followers, friends, polarity, subjectivity])

    counter = counter + 1
    if (counter == target_num):
        break

csvFile.close()