total_cost = float(input("What is the cost of your dream house? "))
annual_salary = float(input("Input annual salary: "))
portion_saved = float(input("Input monthly savings as a decimal: "))
portion_down_payment = total_cost * 0.25  # down payment is 25% of house price
semi_annual_raise = float(input("Input your 6 monthly raise as a decimal: "))
r = 0.04  # interest rate
current_savings = 0
months = 0
while current_savings <= portion_down_payment:
    monthly_salary = annual_salary / 12  # annual salary divided by 12 needs to be inside while loop for increases
    current_savings += (portion_saved * monthly_salary) + current_savings*(r/12)
    months += 1
    if months % 6 == 0:  # adds salary raise every 6 months
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)
print("Number of months required: " + str(months))
