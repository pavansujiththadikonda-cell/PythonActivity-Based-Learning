# Case Study 08: Employee Salary Calculator

print("===== Employee Salary Calculator =====")

employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))

hra = basic_salary * 0.20
da = basic_salary * 0.10
bonus = basic_salary * 0.05

gross_salary = basic_salary + hra + da + bonus

if gross_salary >= 50000:
    tax = gross_salary * 0.10
else:
    tax = gross_salary * 0.05

net_salary = gross_salary - tax

print("\n===== Salary Report =====")
print("Employee Name:", employee_name)
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("Bonus:", bonus)
print("Gross Salary:", gross_salary)
print("Tax:", tax)
print("Net Salary:", net_salary)

print("==============================")
