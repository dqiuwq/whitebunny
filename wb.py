# wb.py
# ----------------------------------------------------------------------
# Author: 		Desmond Qiu
# Version:		1.0
# Date:			28/07/2019
#				Started
# ----------------------------------------------------------------------
# Description: 	To get and validate user input
# Input: 		The title to be displayed during prompt
# Return: 		The input value
def getInput(title):
	while True:
		try:
			print(f'{title}')
			n = float(input(f'Please enter amount (S$): '))
		except ValueError:
			print('Sorry, invalid value')
		else:
			if n < 0:
				print('Sorry, positive only')
			else:
				return n
				break
# ----------------------------------------------------------------------
# Description: 	To get the interest rate amount based on the salary
#				credited plus one category transaction
# Input: 		The eligible amount
# Return: 		The interest rate
def cat1(amount):
	#print('category 1')
	#if >= 2000 < 2500 then 1.55
	if (amount >= 2000 and amount < 2500):
		rate = 1.55
	#if >= 2500 < 5000 then 1.85
	elif (amount >= 2500 and amount < 5000):
		rate = 1.85
	#if >= 5000 < 15k then 1.9
	elif (amount >= 5000 and amount < 15000):
		rate = 1.9
	#if >= 15k  < 30k then 2.0
	elif (amount >= 15000 and amount < 30000):
		rate = 2.0
	#if >= 30k then 2.08
	elif (amount >= 30000):
		rate = 2.08
	return rate
# ----------------------------------------------------------------------
# Description: 	To get the interest rate amount based on the salary
#				credited plus two category transaction
# Input: 		The eligible amount
# Return: 		The interest rate
def cat2(amount):
	#print('category 2')
	#if >= 2000 < 2500 then 1.80
	if (amount >= 2000 and amount < 2500):
		rate = 1.8
	#if >= 2500 < 5000 then 2.00
	elif (amount >= 2500 and amount < 5000):
		rate = 2.0
	#if >= 5000 < 15k then 2.2
	elif (amount >= 5000 and amount < 15000):
		rate = 2.2
	#if >= 15k  < 30k then 2.3
	elif (amount >= 15000 and amount < 30000):
		rate = 2.3
	#if >= 30k then 3.5
	elif (amount >= 30000):
		rate = 3.5
	return rate
# ----------------------------------------------------------------------
# Description: 	Applicable for balance on next 50k.
#				To get the interest rate amount based on the salary
#				credited plus three or more category transaction.
# Input: 		The eligible amount
# Return: 		The interest rate
def cat3(amount):
	#print('category 3')
	#if < 2000 then 0.05
	if (amount < 2000):
		rate = 0.05
	#if >= 2000 < 2500 then 2.0
	elif (amount >= 2000 and amount < 2500):
		rate = 2.0
	#if >= 2500 < 5000 then 2.2
	elif (amount >= 2500 and amount < 5000):
		rate = 2.2
	#if >= 5000 < 15k then 2.4
	elif (amount >= 5000 and amount < 15000):
		rate = 2.4
	#if >= 15k  < 30k then 2.5
	elif (amount >= 15000 and amount < 30000):
		rate = 2.5
	#if >= 30k then 3.8
	elif (amount >= 30000):
		rate = 3.8
	return rate
# ----------------------------------------------------------------------
# Description: 	To calculate the monthly interest rate based on annual
#				interest rate.
# Input: 		The annual interest rate
# Return: 		The monthly interest rate
def getMonthIntRate(annualRate):
	return annualRate/12 #(annualRate)*30.416/365
# ----------------------------------------------------------------------
# Description:	To calculate total interest earned
# Input:		The balance amount
# 				The interest rate
# Return:		Total interest earned
def getTotalIntEarn(bal, rate):
	return (bal * getMonthIntRate(rate))/100
# ----------------------------------------------------------------------
# Description: 	To output the results for first and next 50k
# Input: 		The total eligible transaction
#				The first 50k interest rate
#				The second 50k interest rate
#				The balance amount
#				The next amount
def printResult(trans, first_rate, second_rate, total):
	print(f'Eligible transaction (S$): {trans:.2f}')
	
	if second_rate > 0:
		print(f'Eligible interest rate (first 50k): {first_rate:.2f}%')
		print(f'Eligible interest rate (next 50k): {second_rate:.2f}%')
	else:
		print(f'Eligible interest rate (first 50k): {first_rate:.2f}%')
	
	print(f'Total interest earned per month (S$): {total:.2f}')
# ----------------------------------------------------------------------
#start of program
#collect user data
balance = float(getInput('Account balance'))
salary = float(getInput('Salary amount'))
creditCard = float(getInput('Credit card spent'))
homeLoan = float(getInput('Home loan amount'))
insurance = float(getInput('Insurance'))
investment = float(getInput('Investment'))

#put into array
categories = [creditCard, homeLoan, insurance, investment]
#for calculation purpose
count = 0 #number of cate fulfilled
total_transaction = 0.0 #sum of all cate
rate = 0.0 #interest rate
# processing
for c in categories:
	if c > 0: #fulfilment criteria
		total_transaction += c
		count += 1 #increse count by 1 if cate fulfil
#print(f'categories: {count}')
total_transaction += salary

if salary <= 0:
	rate = 0.05
	total = getTotalIntEarn(balance, rate)
	printResult(total_transaction, rate, 0, total)
elif balance > 50000 and count >= 3:
	if total_transaction < 2000:
		first_rate = 0.05
		second_rate = 0.05
	elif total_transaction >= 2000:
		first_rate = float(cat2(total_transaction))
		second_rate = float(cat3(total_transaction))

	first = 50000.0
	next = float(balance - first)
	total = getTotalIntEarn(first, first_rate)
	total = total + getTotalIntEarn(next, second_rate)
	printResult(total_transaction, first_rate, second_rate, total)
elif balance > 50000: # max 2 category
	if total_transaction < 2000:
		first_rate = 0.05
		second_rate = 0.05
	elif total_transaction >= 2000:
		if count == 0:
			first_rate = 0.05
		elif count == 1:
			first_rate = float(cat1(total_transaction))
		elif count == 2:
			first_rate = float(cat2(total_transaction))
		second_rate = 0.05 #fixed rate

	first = 50000.0
	next = float(balance - first)
	total = getTotalIntEarn(first, first_rate)
	total = total + getTotalIntEarn(next, second_rate)
	printResult(total_transaction, first_rate, second_rate, total)
else: # first 50k
	if total_transaction < 2000:
		#print('You get 0.05%')
		rate = 0.05
	elif total_transaction >= 2000:
		if count == 0:
			rate = 0.05
		elif count == 1:
			rate = float(cat1(total_transaction))
		elif count == 2:
			rate = float(cat2(total_transaction))
		else:
			rate = float(cat2(total_transaction))

	total = getTotalIntEarn(balance, rate)
	printResult(total_transaction, rate, 0, total)
#end tma.py
