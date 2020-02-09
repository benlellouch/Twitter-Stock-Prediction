"""
	This class deals with taking a data set of sentiment analysis on a company, at any one time and then calculating the change of stock price based on that sentiment
	Have a seperate thread running in the background dealing with a company's live stock price that we can get data from to apply to the stock price change 
	Produce values of the predicted stock price based on the sentiment analysis
"""
import datetime
import math
"""
	this class made me want to die - honestly 
"""
class StockPrediction :

	def __init__(self) :
		pass 

	def stonks_bash(self,data_set) :
	#forecast_value = forecast_function(data_set)
		return self.forecast_function(data_set)

	"""
		forecasts the trend of the stock market by comparing the similarity in positive 
		sentiment in the 
	"""
	def forecast_function(self,data_set) :
		positive_data_sum = 0
		negative_data_sum = 0
		for positive_data_value in self.positive_data(data_set) :
			positive_data_sum = positive_data_sum + (self.time(positive_data_value)*self.SSM(data_set,[positive_data_value]))
		#print(positive_data_sum)

		for negative_data_value in self.negative_data(data_set) :
			negative_data_sum = negative_data_sum + (self.time(negative_data_value)*self.SSM(data_set,[negative_data_value]))
		#print(negative_data_sum)
		return (positive_data_sum - negative_data_sum)

	"""
		auxilliary time function that depreciates the relevance of a tweet if
		it was posted a long time ago 
	"""
	def time(self,data_set_value) : 
		days = datetime.datetime.today().day - data_set_value[1].day
		return (1-(0.2*days)) if days < 5 else 0


	"""
		partitions the data set into the negative sentiment data set 
	"""
	def negative_data(self,data_set) :
		negative_data_set = []
		for tweet_time in data_set :
			if tweet_time[0] < 0.0 :
				negative_data_set.append(tweet_time)
		return negative_data_set

	"""
		partitions the data set into the positive sentiment data set 
	"""
	def positive_data(self,data_set) :
		positive_data_set = []
		for tweet_time in data_set :
			if tweet_time[0] > 0.0 :
				positive_data_set.append(tweet_time)
		return positive_data_set


	def sum_of_x_squared(self,data_set) :
		x_squared_sum = 0
		for tweet_time in data_set :
			x_squared_sum = x_squared_sum + (tweet_time[0])**2
		return x_squared_sum


	def mu_value(self,data_value_1,data_value_2) :
	#print(type(data_value_1), type(data_value_2))
		if abs(data_value_1[0] - data_value_2[0]) >= 1 :
			return 0
		else :
			return 1 - abs(data_value_1[0] - data_value_2[0])

	"""
		fuck python - haskell is better (basically the haskell take function)
	"""	
	def take(self,size, data_set) :
		reverse_list = data_set[::-1]
		new_list = reverse_list[size:]
		return new_list[::-1]


	"""
		System Similarity Model 
		data_set_1 has a cardinality of m, data_set_2 has a cardinality of n
	"""
	def SSM(self,data_set_1, data_set_2) :	
		p = len(data_set_1) if len(data_set_1) < len(data_set_2) else len(data_set_2)

		#dealing with the square root of the summation of x^2 values
		x_sum = math.sqrt(self.sum_of_x_squared(data_set_1))

		data_set_1_up_to_p = self.take((p-1), data_set_1)
		data_set_2_up_to_p = self.take((p-1), data_set_2)

		#dealing with the summation of x^2_i * mu_i from 1 to p
		x_squared_with_mu_sum = 0
		for set_1_values in data_set_1_up_to_p :
			for set_2_values in data_set_2_up_to_p :
				x_squared_with_mu_sum = x_squared_with_mu_sum + (self.mu_value(set_1_values,set_2_values) * (set_1_values[0])**2)

		#dealing with summation of x^2_i * mu^2_i from 1 to p
		x_squared_with_mu_squared_sum = 0
		for set_1_values in data_set_1_up_to_p :
			for set_2_values in data_set_2_up_to_p :
				x_squared_with_mu_squared_sum = x_squared_with_mu_squared_sum + ((self.mu_value(set_1_values,set_2_values))**2 * (set_1_values[0])**2)

		#dealing with the summation of y^2 from p+1 to n
		y_squared_up_to_p_sum = 0
		y_squared_sum = 0

		#y squared from 1 to n
		for data_set_2_values in data_set_2 :
			y_squared_sum = y_squared_sum + (data_set_2_values[0])**2

		for data_set_2_up_to_p_values in data_set_2_up_to_p :
			y_squared_up_to_p_sum = y_squared_up_to_p_sum + (data_set_2_up_to_p_values[0])**2

		y_squared_from_p_to_n = y_squared_sum - y_squared_up_to_p_sum


		mu_sum = 0
		for set_1_values in data_set_1_up_to_p :
			for set_2_values in data_set_2_up_to_p :
				mu_sum = mu_sum + self.mu_value(set_1_values,set_2_values)

	
		"""	
		print("mu sum: ", mu_sum)
		print("size of data set 1: ", len(data_set_1))
		print("size of data set 2: ", len(data_set_2))
		print("x^2 with mu sum: ", x_squared_with_mu_sum)
		print("square root of data set 1: ", math.sqrt(len(data_set_1)))
		print("x sum: ", x_sum)
		print("square root x^2*mu_sum + y^2: ", math.sqrt(x_squared_with_mu_squared_sum + y_squared_from_p_to_n))
		"""
		if mu_sum == 0 :
			return 0
		else :
			return x_squared_with_mu_sum / (math.sqrt(len(data_set_1)) * x_sum * math.sqrt(x_squared_with_mu_squared_sum + y_squared_from_p_to_n))

	
		
		
#Testing Area

data_set = [(-1, datetime.datetime(2020, 2, 6, 16, 7, 46)),(-1, datetime.datetime(2020, 2, 6, 16, 7, 46)),(-1, datetime.datetime(2020, 2, 6, 16, 7, 46)),(-1, datetime.datetime(2020, 2, 6, 16, 7, 46)),(-1, datetime.datetime(2020, 2, 6, 16, 7, 46)),(-1, datetime.datetime(2020, 2, 6, 16, 7, 46)),(-1, datetime.datetime(2020, 2, 6, 16, 7, 46)),(-1, datetime.datetime(2020, 2, 6, 16, 7, 46)),(-1, datetime.datetime(2020, 2, 6, 16, 7, 46)), (-1, datetime.datetime(2020, 2, 6, 16, 7, 46)),(-1, datetime.datetime(2020, 2, 6, 16, 8, 46)), (-1, datetime.datetime(2020, 2, 3, 16, 7, 43)), (-1, datetime.datetime(2020, 2, 8, 16, 7, 43)), (-1, datetime.datetime(2020, 2, 8, 16, 7, 42)), (-1, datetime.datetime(2020, 2, 8, 16, 7, 41)), (-1, datetime.datetime(2020, 2, 8, 16, 7, 41)), (-1, datetime.datetime(2020, 2, 8, 16, 7, 41))] 
data_set_1 = [(0.6369, datetime.datetime(2020, 2, 8, 16, 8, 10)), (0.2023, datetime.datetime(2020, 2, 8, 16, 8, 10)), (0.34, datetime.datetime(2020, 2, 8, 16, 8, 9)), (0.5106, datetime.datetime(2020, 2, 8, 16, 8, 9))]
#print(negative_data(data_set))
#print(sum_of_x_squared(data_set))
stockPredict = StockPrediction()
positive_data_set = stockPredict.positive_data(data_set)
negative_data_set = stockPredict.negative_data(data_set)


#print("SSM data set against positive data set:")
print("POSITIVE: ")
print(stockPredict.SSM(data_set,positive_data_set))
print("NEGATIVE: ")
print(stockPredict.SSM(data_set,[negative_data_set[1]]))
print("TOTAL: ")
print("stock market change:",stockPredict.stonks_bash(data_set), "%")
#print("SSM positive data against whole data set:")
#print(SSM(positive_data_set,data_set))
#print("SSM data set against data set 1:")
#print(SSM(data_set,data_set_1))
#print("mu Value:")
#print(mu_value((0.4413, datetime.datetime(2020, 2, 6, 16, 7, 46)),(1.0000, datetime.datetime(2020, 2, 8, 16, 8, 10))))

#print("forecast: ",forecast_function(data_set_1), "%")

#print(mu_value((0.5413, datetime.datetime(2020, 2, 6, 16, 7, 46)),(0.2023, datetime.datetime(2020, 2, 8, 16, 8, 10))))
