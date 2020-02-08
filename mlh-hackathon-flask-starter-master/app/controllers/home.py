# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, jsonify, request
from yahoo_fin import stock_info as sf


blueprint = Blueprint('home', __name__)


def get_score(ticker):
	if ticker == 'AAPL': return 0.63


def is_positive(score):
	if score > 0: return True
	else: return False




@blueprint.route('/', methods=['GET', 'POST'])
def index():
	# if request.method == 'GET':
	# 	pass
	# if request.method == 'POST':
	# 	# get the form details
	if True:
		selected_stock_ticker = 'AAPL'

		# score
		score = get_score(selected_stock_ticker)
		# Feedback
		feedback = is_positive(score)
		# Stock price
		ticker_price = sf.get_live_price("AAPL")
		return jsonify([score, feedback, ticker_price])
		return render_template('home/index.html')


