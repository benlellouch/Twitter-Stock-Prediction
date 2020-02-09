# HackTheSouth20
## Introduction
Welcome to the WhiteStockPartnership HackTheSouth20 project!
### What is our project about?
Our application basically uses social media to try and predict market trends of stocks in the S&P 100 index.
### How does it work?
#### twitter fetcher
It starts by fetching 100 tweets where a company X is mentioned and formats the tweets into a list of tuples (tweet content, datetime of tweet).
#### Sentiment Analyser
The fetched tweets then go into a sentiment analyser which produces of list of tuples (tweet intensity score, datetime of tweet).
