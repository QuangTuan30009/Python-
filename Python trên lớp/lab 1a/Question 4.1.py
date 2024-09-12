def batphan(decimal_number):
    if decimal_number == 0:
        return "0"
    
    octal_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 8
        octal_number = str(remainder) + octal_number
        decimal_number = decimal_number // 8
    
    return octal_number

decimal_number = 65
octal_number = batphan(decimal_number)
print("The octal representation of",decimal_number ,"is", octal_number)
