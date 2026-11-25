# Case Study 02: Warehouse Inventory Reconciliation

print("===== Warehouse Inventory Reconciliation =====")

# Enter inventory details
product_name = input("Enter product name: ")
expected_stock = int(input("Enter expected stock quantity: "))
actual_stock = int(input("Enter actual stock quantity: "))

# Calculate stock difference
difference = actual_stock - expected_stock

print("\n===== Inventory Report =====")
print("Product Name:", product_name)
print("Expected Stock:", expected_stock)
print("Actual Stock:", actual_stock)

if difference == 0:
    print("Status: Stock Matched")
elif difference > 0:
    print("Status: Surplus Stock")
    print("Extra Items:", difference)
else:
    print("Status: Stock Shortage")
    print("Missing Items:", abs(difference))

print("===========================================")