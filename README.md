# White Stock Sentiment Analysis 

We are White Stock, a Hackathon start up team for the Hack the South 2020! We use some Sentiment Analysis, some fancy maths, and some computer magic we provide meaningful information to plan your next move in the market!

We use the general opinion of the public expressed on social media about companies to predict market trends of stocks in the S&P 100 index.

### How does it work?
#### twitter fetcher
It starts by fetching 100 tweets where a company X is mentioned and formats the tweets into a list of tuples (tweet content, datetime of tweet).
#### Sentiment Analyser
The fetched tweets then go into a sentiment analyser which produces of list of tuples (tweet intensity score, datetime of tweet).

### Prerequisites

You will need to have tweepy and nltk 
```
pip3 install tweepy 
```
```
pip3 install nltk 
```
### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo
## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```
## Built With

* [vader](https://github.com/cjhutto/vaderSentiment) - The Sentiment Analysis API used 
* [tweepy](https://www.tweepy.org) - The Twitter API used
* [pyplot](https://matplotlib.org/api/pyplot_api.html) - matplotlib library to build graphs of sentiment analysis
* [json](https://docs.python.org/3/library/json.html) - python library to read and write JSON files

## Versioning

We use [GitHub](http://github.com/) for versioning.

## Authors

* **Behrad Koohy** - *Dev Ops* - [behradkoohy](https://github.com/behradkoohy)
* **Benjamin Lellouch** - *Principal Back End Developer* - [benlellouch](https://github.com/benlellouch)
* **Benjamin Rees** - *Statistical Work and Development of Market Prediction algorithm* - [BenWRees](https://github.com/BenWRees)
* **Michael Gimson** - *Persistent Data Development* - [MichaelGimson](https://github.com/MichaelGimson)
* **Jury D'Alessio** - *Principal Front End Developer* - [JuryDAlessio](https://github.com/JuryDAlessio)
* **Isreal Geniuss** - *Man who chats bollocks on Twitter* - N/A



