def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return f"The final price after a {discount_percent}% discount is: {final_price}"
    else:
        return f"Discount is too low to give a discount. The original price is: {price}"

# enter input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and display the result
result = calculate_discount(price, discount_percent)
print(result)
