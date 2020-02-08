"""
	This class deals with taking a data set of sentiment analysis on a company, at any one time and then calculating the change of stock price based on that sentiment

	Have a seperate thread running in the background dealing with a company's live stock price that we can get data from to apply to the stock price change 

	Produce values of the predicted stock price based on the sentiment analysis
"""
import datetime

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


def sum_of_x_squared(data_set) :
	x_squared_sum = 0
	for tweet_time in data_set :
		x_squared_sum = x_squared_sum + (tweet_time[0])**2
	return x_squared_sum

def mu_value(data_point_1,data_point_2) :
	return 0 if (1-abs(data_point_1 - data_point_2)) < 0 else 1-abs(data_point_1 - data_point_2)
	


"""
	System Similarity Model 
"""
def SSM(data_set_1, data_set_2) :
	p = len(data_set_1) if len(data_set_1) < len(data_set_2) else len(data_set_2)
	x_sum = sqrt(sum_of_x_squared(data_set_1))
	
	
		
		
#Testing Area
data_set = [(0.5413, datetime.datetime(2020, 2, 6, 16, 7, 46)), (-0.4939, datetime.datetime(2020, 2, 3, 16, 7, 43)), (0.8832, datetime.datetime(2020, 2, 8, 16, 7, 43)), (-0.34, datetime.datetime(2020, 2, 8, 16, 7, 42)), (0.7034, datetime.datetime(2020, 2, 8, 16, 7, 41)), (-0.0258, datetime.datetime(2020, 2, 8, 16, 7, 41)), (-0.1027, datetime.datetime(2020, 2, 8, 16, 7, 41)), (0.4588, datetime.datetime(2020, 2, 8, 16, 7, 41)), (0.4019, datetime.datetime(2020, 2, 8, 16, 7, 40))] 
for data_set_point in data_set :
	print(time(data_set_point))
#print(negative_data(data_set))
print(sum_of_x_squared(data_set))

