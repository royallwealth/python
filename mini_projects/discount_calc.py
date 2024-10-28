# DISCOUNT CALCULATOR 🧮
# Samantha S.

print("""
   88             88 88                        
         88             88 88                        
         88             88 88                        
 ,adPPYb,88  ,adPPYba,  88 88 ,adPPYYba, 8b,dPPYba,  
a8"    `Y88 a8"     "8a 88 88 ""     `Y8 88P'   "Y8  
8b       88 8b       d8 88 88 ,adPPPPP88 88          
"8a,   ,d88 "8a,   ,a8" 88 88 88,    ,88 88          
 `"8bbdP"Y8  `"YbbdP"'  88 88 `"8bbdP"Y8 88          
                                                
      """)

print("Welcome to the in-store discount calculator!🚪")

# user inputs
price = float(input("What is the total bill?\n$"))
discount = int(input("Which coupon would you like to apply? 5%, 10%, or 20%:\nCoupon: "))

# stored calculation discount % divided out of 100% times the price gives the discount amount
# the final amount is the price - the discount

discount_amount = round(discount / 100 * price)
final_amount = round(price - discount_amount, 2)

# print the final calculations
print(f"Discount: ${discount_amount}")
print(f"Final Bill: ${final_amount}")


