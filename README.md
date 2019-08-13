# Week 5 Task 1

Your task is to implement the algorithms to calculate and validate check digits for different kinds of barcodes.

You must calculate and validate the check digit for:

- Credit Cards

And choose one or more of:

- ISBN-10 Books
- ISBN-13 Books
- GTIN-13 Product Codes

To help you get started:

- How to calculate ISBN-10 check digits: https://isbn-information.com/the-10-digit-isbn.html
- How to calculate ISBN-13 check digits https://isbn-information.com/check-digit-for-the-13-digit-isbn.html
- A list of test credit card numbers https://support.paya.com/44616-sage-virtual-terminal-not-done/315930-list-of-test-card-numbers
- The algorithm used to calculate the check digit for credit card numbers https://en.wikipedia.org/wiki/Luhn_algorithm



## GTIN-13 check digits are calculated as follows:

Multiply every second digit by 3, and every other digit by 1.
Add up all the multiplied numbers.
You can now get the check digit by working out what number would have to be added to the
sum in order to bring it up to a multiple of 10. If the number is already a multiple of 10, the check digit is 0.


## ISBN-10 check digits are calculated as follows:

Multiply the first digit in the barcode by 10. Add the result to the sum.
Multiply the second digit in the barcode by 9. Add the result to the sum.
Multiply the third digit in the barcode by 8. Add the result to the sum.
....
Multiply the last number in the barcode by 1. Add the result to the sum.
Calculate the remainder of the sum when divided by 11.
The check digit is 11 minus the remainder of the result in step 6 when divided by 11. If the check digit is 10, it is replaced with an ‘X’.


## Running your program:

If I provide this input:

```
print(calculate_gtin13_barcode_check_digit('940055061977'))
```

The output I expect is:

```
5
```

If I provide this input:

```
print(validate_gtin13_barcode_check_digit('9400550619775'))
```

The output I expect is:

```
This is a valid gtin13 barcode.
```


The only thing that should change is the name of the function dependant on the type of barcode (i.e. gtin13, isbn10, isbn13 or credit_card).



Note: obviously your code should handle more test cases than just the two I provided, these are just examples to demonstrate how I expect to be able to call your code). 
