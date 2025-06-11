# Input section
name = input("Enter your name: ")
product = input("Enter the product name: ")
quantity = int(input("Enter the quantity: "))
price_per_unit = float(input("Enter the price per unit: "))

# Calculating total amount
total_price = quantity * price_per_unit

# Discount calculation
if total_price >= 5000:
    discount = total_price * 0.20  #20% discount
elif total_price >= 2000:
    discount = total_price * 0.10  #10% discount
else:
    discount = 0                   #No discount

# Delivery charge
delivery_charge = 100 if quantity > 10 else 0

# Final bill calculation
final_amount = total_price - discount + delivery_charge

# Output formatted bill
print("\n====== Final Bill ======")
print(f"Customer Name     : {name}")
print(f"Product           : {product}")
print(f"Quantity          : {quantity}")
print(f"Price per Unit    : ₹{price_per_unit}")
print(f"Total Price       : ₹{total_price}")
print(f"Discount Applied  : ₹{discount}")
print(f"Delivery Charges  : ₹{delivery_charge}")
print(f"Final Amount Payable: ₹{final_amount}")
print("========================")
