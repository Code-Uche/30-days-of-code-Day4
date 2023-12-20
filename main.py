# This a simple earnings calculator that will calculate employee's earnings
employee_name=input("What is your name? ".strip().title())
hourly_wage=input("What is your hourly wage?")
hours_worked=input("How many hours did you work this week?")

earnings=(float(hours_worked) * float(hourly_wage))
print(f"{employee_name} earned ${earnings} this week." .strip().title())