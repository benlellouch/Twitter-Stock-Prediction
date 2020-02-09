# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, jsonify, request
from yahoo_fin import stock_info as sf

import json
import os


blueprint = Blueprint('home', __name__)


def get_score(ticker):
	if ticker == 'AAPL':
		return 0.63
	else:
		return 0.45




def calculate_accuracy(ticker):
	with open('../accuracy.json') as f:
		data = json.loads(f.read())
	return data[ticker]


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
	selected_data['price'] = '%.2f' % (sf.get_live_price(selected_stock_ticker))
	# selected_data['open'] = '%.2f' % (sf.get_open(selected_stock_ticker))
	selected_data['score'] = get_score(selected_stock_ticker)
	selected_data['accuracy'] = '%.2f' % calculate_accuracy(selected_stock_ticker)
	selected_data['tweets'] = ""


	return render_template('home/index.html', stonks=company_data, data=selected_data)
