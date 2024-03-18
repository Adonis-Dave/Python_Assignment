def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_price = price - (price * (discount_percent / 100))
        return discount_price
    else:
        return price


price = int(input("Enter the product's original price: "))
discount_percent = int(input("Enter the discount price of the product: "))
final_price = calculate_discount(price, discount_percent)

print(final_price)
