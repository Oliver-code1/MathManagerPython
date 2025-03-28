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

		elif (income > 12570 and 



	
	def calculate_monthly_interest(principal, annual_rate, years):
    """
    Calculate the monthly interest gained for a savings account.

    :param principal: The initial amount of money deposited (float).
    :param annual_rate: The annual interest rate in percentage (float).
    :param years: The number of years the money is saved (int).
    :return: Monthly interest gained (float).
    """
    # Convert annual rate to decimal
    annual_rate_decimal = annual_rate / 100

    # Calculate total interest for the given years
    total_interest = principal * annual_rate_decimal * years

    # Calculate monthly interest
    monthly_interest = total_interest / (years * 12)

    return monthly_interest
