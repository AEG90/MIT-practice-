# Problem Set 2
#-----------------------------

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save: '))
total_cost = float(input('Enter the cost of home: '))
sar = float(input('Enter your raise amount: '))
pdp = .25 * total_cost       # portion of down payment.
current_savings = 0
numMonths = 0

while current_savings <= pdp:
   monthly_savings = (annual_salary/12)
   current_savings = current_savings + monthly_savings*portion_saved+ (current_savings * .04)/12
   numMonths +=1
   if numMonths % 6 == 0:
        annual_salary = annual_salary + (annual_salary * sar)
print('Number of months: ',numMonths)
