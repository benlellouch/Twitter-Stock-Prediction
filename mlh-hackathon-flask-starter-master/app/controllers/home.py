# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, jsonify, request
from yahoo_fin import stock_info as sf

import json
import os


blueprint = Blueprint('home', __name__)


def get_score(ticker):
    with open("../date&score-pairs.json", "r") as f:
        data = json.loads(f.read())
    key = max(data.keys())
    for dict in (data[key]):
        if(dict.get(ticker)):
            return dict.get(ticker)


def get_prediction(ticker):
    with open("../predictions.json", "r") as f:
        data = json.loads(f.read())
    key = max(data.keys())
    for dict in (data[key]):
        if(dict.get(ticker)):
            return dict.get(ticker)


def calculate_accuracy(ticker):
    with open('../accuracy.json') as f:
        data = json.loads(f.read())
    return data[ticker]


def get_image(ticker):
    image_path = "static/" + ticker + ".png"
    return image_path


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    print('index')
    selected_stock_ticker = 'AAPL'

    if request.method == 'GET':
        print('GET')

    if request.method == 'POST':
        print('dasd')
        ticker = (str(request.form['selected']).strip()[-16::]).strip()
        print(ticker)
        selected_stock_ticker = ticker

    company_data = {}
    selected_data = {}

    with open('../data.json') as f:
        company_data = json.loads(f.read())

    selected_data['ticker'] = selected_stock_ticker
    selected_data['name'] = company_data[selected_stock_ticker]
    selected_data['price'] = '%.2f' % (
        sf.get_live_price(selected_stock_ticker))
    # selected_data['open'] = '%.2f' % (sf.get_open(selected_stock_ticker))
    selected_data['score'] = get_score(selected_stock_ticker)
    selected_data['accuracy'] = '%.2f' % calculate_accuracy(
        selected_stock_ticker)
    selected_data['tweets'] = ""
    selected_data['prediction'] = get_prediction(selected_stock_ticker)
    selected_data['plot'] = get_image(selected_stock_ticker)

    return render_template('home/index.html', stonks=company_data, data=selected_data)
