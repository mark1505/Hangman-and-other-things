total_cost = float(input("What is the cost of your dream house? "))
annual_salary = float(input("Input annual salary: "))
monthly_salary = annual_salary / 12  # annual salary divided by 12
portion_saved = float(input("Input monthly savings as a decimal: "))
portion_down_payment = total_cost * 0.25  # down payment is 25% of house price
r = 0.04  # interest rate
current_savings = 0
months = 0
while current_savings <= portion_down_payment:
    current_savings += (portion_saved * monthly_salary) + current_savings*(r/12)
    months += 1
print("Number of months required: " + str(months))
