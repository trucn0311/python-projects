# Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many
# decimal places. Keep a limit to how far the program will go.
# 📌 Example:
# If N = 2 → π = 3.14
# If N = 10 → π = 3.1415926535
# If N = 50 → π = 3.14159265358979323846264338327950288419716939937510

from decimal import Decimal, getcontext

def calculate_pi(digits):
    # Set the precision (how many digits we want). We add 2 extra digits to be safe during rounding.
    getcontext().prec = digits + 2  
    arctan_1_5 = arctan(Decimal(1)/5, digits)
    arctan_1_239 = arctan(Decimal(1)/239, digits)
    pi = 16 * arctan_1_5 - 4 * arctan_1_239
    return pi

# This function calculates arctangent using something called a Taylor Series (
def arctan(x, terms):
    # Start with a total of 0.
    total = Decimal(0)
    # Keeps track of x raised to powers (x¹, x³, x⁵, ...)
    x_power = x
    # Repeat the math a certain number of times (how many “terms” to include for accuracy).
    for n in range(terms):
        term = x_power / (2*n + 1)
        total += term if n % 2 == 0 else -term
        x_power *= x * x
    return total

def cal_digit():
    digits = int(input('Choose the number: '))
    if digits <= 50:
        pi = calculate_pi(digits)
        # Prints only the number of digits you asked for.
        print(str(pi)[:digits + 2])  # "3." + digits
    else:   
        print('Number cannot be larger than 50')

cal_digit()
