# Problem Set 1

# Assign all the values
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save: '))
total_cost = float(input('Enter the cost of home: '))
monthly_savings = (annual_salary/12)*(portion_saved)
pdp = .25
a_return = .04
current_savings = 0
down_payment = total_cost * pdp
numMonths = 0

# Set a while loop with current savings to grow, up until the amount of your downpayment total.
while current_savings < down_payment:   
# Add up your total savings, broken down to each month.
    current_savings += monthly_savings + ((current_savings * a_return)/12)
#add each month it takes to get to your downpayment.
    numMonths +=1
print('Number of months: {}'.format(numMonths))




