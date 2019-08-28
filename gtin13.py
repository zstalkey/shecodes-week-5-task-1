# ## GTIN-13 check digits are calculated as follows:

# 1. Multiply every second digit by 3, and every other digit by 1.
# 2. Add up all the multiplied numbers.
# 3. You can now get the check digit by working out what number would have to be added to the sum in order to bring it up to a multiple of 10.
# If the number is already a multiple of 10, the check digit is 0.

# The test files assume:
# - Your functions are named:
#     - `calculate_gtin13_barcode_check_digit()`
#     - `validate_gtin13_barcode_check_digit()`


def split (validate_gtin13_barcode_check_digit):
    return list (validate_gtin13_barcode_check_digit)
validate_gtin13_barcode_check_digit = input('Please input an ISBN-13 number: ')
# print(split(validate_gtin13_barcode_check_digit))
#this is to take the input and split and turn into a list

totalodd = 0
totaleven = 0
gtin13_sum = 0
gtin13_sum2 = 0
# gtin13_sum3 = 0
checkdig = 0

for counter, number in enumerate(validate_gtin13_barcode_check_digit,1): #identifying a counter and the value
    number = int(number) #turning the number into a integer to be able to calculate the formula
    if counter %2 == 0: #starting from 1, if the counter is even (index odd) multiply the number by 3
        gtin13_sum = (number*3)
        totalodd += gtin13_sum
        # print(totalodd)
    elif counter == 13: #finding the value of the 13th counter (12th number) as this is not included in the formula sum
        gtin13_sum2 = (number*1)
        checkdig += gtin13_sum2 #note a value of two is being given to gtin13_sum2 but not put into total odd or totaleven, so two is removed from the equation :):):)
    #     # print(checkdig)
    else: 
        totaleven += number
        # print(totaleven)

calculate_gtin13_barcode_check_digit = (10-((totalodd + totaleven)%10))
# print(calculate_gtin13_barcode_check_digit)

if calculate_gtin13_barcode_check_digit == checkdig:
    print('This is a valid ISBN number')
else:
    print('This is an invalid ISBN number')
        
