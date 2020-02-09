# import plotly.graph_objects as go
import matplotlib.pyplot as plt
import os
import json

def generate_graph(f, ticker):
    if not os.path.exists("plots"):
        os.mkdir("plots")
    x_plot = []
    y_plot = []
    file = open(f,"r").read()
    json_file = json.loads(file)
    for (k,list_dicts) in zip(json_file.keys(), json_file.values()):
        for dict in list_dicts:
            if (dict.get(ticker)):
                x_plot.append(k)
                y_plot.append(dict.get(ticker))
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.plot(x_plot,y_plot)
    plt.title("Average Popularity Score of " + ticker)
    plt.xlabel("Epoch Time")
    plt.ylabel("Average Popularity Score")

    fig.savefig("plots/" + ticker + ".png")
