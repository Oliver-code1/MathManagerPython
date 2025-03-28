class mathmanager:

	def add(self, a, b):
			return a+b

	def subtract(self, a, b):
			return a-b

	def multiply(self, a, b):
			return a*b

	#The test below is wrong
	def interest (self, principal, annual_rate, years):
		b= principal * annual_rate * years
		monthly_interest = b / (years *12)
		return monthly_interest

	#This is correct
	def interest(self, deposit, term):
		if deposit <=0:
			return -1
		if term==1:
			return (0.038*deposit)/12
		elif term == 2:
			return (0.036*deposit)/12
		else:
			return -2
		

	def tax(self, income):
		if (income >= 0 and income <= 12570):
			return 0
		elif (income > 12570 and income<= 50270):
			return 20/100*(income- 12570)
		elif (income 



	
	
