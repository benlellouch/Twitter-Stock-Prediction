import datetime
import json
import nltk
# nltk.download('vader_lexicon')
from sentimentAnalyser import TwitterFetcher, SentimentAnalyser
from stockPrediction import StockPrediction
from plotter import generate_graph
from random import random
from random import seed
from random import randint
import time
DEBUG = False

def querySentiment(f):
    tf = TwitterFetcher()
    sa = SentimentAnalyser()
    sp = StockPrediction()
    current_time = time.time()
    time_dict = {}
    pred_dict = {}
    # dictionary of acronym : name
    company_data = json.loads(f.read())
    try:
        with open("date&score-pairs.json", "r") as f:
            time_dict = json.loads(f.read())
            time_dict[current_time] = []
    except Exception:
        time_dict = {current_time: []}
    try:
        with open("predictions.json", "r") as f:
            pred_dict = json.loads(f.read())
            pred_dict[current_time] = []
    except Exception:
        pred_dict = {current_time: []}
    for k in company_data:
        # gets tweets -> tweets analysed
        analysed = sa.analyse(tf.get_tweets(company_data[k], 100))
        if analysed:
        # if True:
            prediction = sp.stonks_bash(analysed)
            if not DEBUG:
                # average score calculated
                avg = sa.average_score(analysed)
            else:
                avg = random()
            print(company_data[k])
            # time : {company, average score}
        time_dict[current_time].append({k:avg})
        pred_dict[current_time].append({k:prediction})
    print(time_dict)
    print(pred_dict)
    with open("date&score-pairs.json", "w") as outfile:
        json.dump(time_dict, outfile)
    with open("predictions.json", "w") as outfile:
        json.dump(pred_dict, outfile)
    for k in company_data:
        generate_graph("date&score-pairs.json", k)


def randomdata(f):
    current_time = time.time()
    dummy_data = {}
    # dictionary of acronym : name
    company_data = json.loads(f.read())
    seed(1)
    dummy_data[current_time] = []
    for k in company_data:
        value = randint(45,70)
        dummy_data[current_time].append({k:value})
    with open("dummydata.json", "w") as outfile:
        json.dump(dummy_data, outfile)

# funky way of being able to serialize datetime
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


# opens json data file
def main():
    with open("data.json", "r") as file:
        querySentiment(file)

if __name__ == "__main__":
    main()
