
#Input must be translated into a list
#create an empty list to use

# - Your functions are named:
#Up to calculating the sum
#     - `calculate_credit_card_number_check_digit()`
#Checking the modulus 10 validation
#     - `validate_credit_card_number_check_digit()`

#User must input a credit card number
#Splits a string into a list
def split (validate_credit_card_number_check_digit):
    return list(validate_credit_card_number_check_digit)
validate_credit_card_number_check_digit = input('Please input your credit card number: ')
# print(split(creditcardnumber))
my_sum=0
my_sum2=0
totalone=0
totaltwo=0
totalthree=0
for counter, number in enumerate(validate_credit_card_number_check_digit,1):
    number = int(number)
    if counter %2 == 0:
        my_sum = (number*2)
        if my_sum > 9:
            my_sum2 = my_sum - 9
            totalone += my_sum2
            # print(totalone)
        else: 
            totaltwo += my_sum
            # print(totaltwo)
    else:
        totalthree += number
        # print(totalthree)

calculate_credit_card_number_check_digit = (totalone + totaltwo + totalthree)
print(calculate_credit_card_number_check_digit)

if calculate_credit_card_number_check_digit % 10 ==0:
    print("valid card number entered")
else: 
    print("invalid card number entered")
