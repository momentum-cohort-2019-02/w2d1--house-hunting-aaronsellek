annual_salary = int(input("Enter annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to save, as a decimal: "))
rate = input("Enter the expected annual rate of return [0.04]: ")
total_cost = int(input("Enter the cost of your dream home: "))
percentage_down = input("Enter the percent of your home's cost to save as a down payment [0.25]: ")

if rate == "":
    rate = .04
else:
    rate = (rate)
if percentage_down == "":
    percentage_down = .25
else:
    percentage_down = float(percentage_down)

portion_down_payment = total_cost * percentage_down
current_savings = 0
monthly_salary = annual_salary / 12
i = 0

monthly_saving = monthly_salary * portion_saved


while current_savings < portion_down_payment:
    investments = current_savings*rate/12
    current_savings = monthly_saving + investments + current_savings
    i += 1

print("Months: " + str(i))
