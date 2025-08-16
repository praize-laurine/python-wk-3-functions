# 1. Creating the funtion
# function name = calculate_discount with parameters(price, discount_percent)

# calcuate the final price after applying the discount

# Dicount =  Price * discountpercent/100

# if discount is >= 20% , dicount = Price * discountpercent/100

# final_price = price -  discount

def calculate_discount(price, discount_percent):
    if discount_percent >= 20 :
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    
    else:
        return price
    

# 2. Prompting the user    
# - To enter the original price of an item and the dicount_percent

# - Print the final price after discount is applied or original price if discount was not applied

price = float(input("Enter Original Price: "))

discount_percent = float(input("Enter percentage discount: "))

final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20 :
    print (f"final_price after {discount_percent}% discount: {final_price:}")

else:
    print(f"No discount applied. Original price: {price:}")
