def is_palindrome(number):
    print(f"original number {number}")
    if str(number) == str(number)[::-1]:
        print("Given number is a palindrome")
    else:
        print("Given number is not a palindrome")

number1 = 1331
is_palindrome(number1)
number2 = 12345
is_palindrome(number2)