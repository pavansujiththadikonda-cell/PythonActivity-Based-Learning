# Case Study 04: Simple Billing & Discount Calculator

print("===== Simple Billing & Discount Calculator =====")

customer_name = input("Enter customer name: ")
item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

total = quantity * price

if total >= 5000:
    discount = total * 0.20
elif total >= 3000:
    discount = total * 0.10
elif total >= 1000:
    discount = total * 0.05
else:
    discount = 0

final_amount = total - discount

print("\n===== Billing Summary =====")
print("Customer Name:", customer_name)
print("Item Name:", item_name)
print("Quantity:", quantity)
print("Price per Item:", price)
print("Total Amount:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)

print("==============================")
