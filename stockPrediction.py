"""
	This class deals with taking a data set of sentiment analysis on a company, at any one time and then calculating the change of stock price based on that sentiment

	Have a seperate thread running in the background dealing with a company's live stock price that we can get data from to apply to the stock price change 

	Produce values of the predicted stock price based on the sentiment analysis
"""

class Stock_Prediction :


	def stonks_bash(data_set) :
		if forecast_function(data_set) > 0:
			return "Stock Increases"
		elif forecast_function(data_set) < 0 :
			return "Stock Deacreases"
		else :
			return "Stock stays the same"

	"""
		forecasts the trend of the stock market by comparing the similarity in positive 
		sentiment in the 
	"""
	def forecast_function(data_set) :
		positive_data_sum = 0
		negative_data_sum = 0
		for positive_data in positive_data(data_set) :
			positive_data_sum = positive_data_sum + (time(positive_data)*SSM(positive_data(data_set),positive_data))

		for negative_data in negative_data(data_set) :
			negative_data_sum = negative_data_sum + (time(negative_data)*SSM(negative_data(data_set),negative_data))
		return positive_data_sum - negative_data_sum

	"""
		auxilliary time function that depreciates the relevance of a tweet if
		it was posted a long time ago 
	"""
	def time(data_set_value) : 
				days = datetime.datetime.today().day - data_set_value[1].day
				return (1-(0.2*days)) if days < 5 else 0


	"""
		partitions the data set into the negative sentiment data set 
	"""
	def negative_data(data_set) :
		negative_data_set = []
		for tweet_time in data_set :
			if tweet_time[0] < 0.0 :
				negative_data_set.append(tweet_time)
		return negative_data_set

	"""
		partitions the data set into the positive sentiment data set 
	"""
	def positive_data(data_set) :

		positive_data_set = []
		for tweet_time in data_set :
			if tweet_time[0] > 0.0 :
				positive_data_set.append(tweet_time)
		return positive_data_set

	"""
		System Similarity Model 
	"""
	def SSM(data_set_1, data_set_point) :
		
		




