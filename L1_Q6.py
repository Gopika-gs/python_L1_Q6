string = input("Enter a string ")
reverse = string [::-1]
if string == reverse:
    print("The string ",string, " is palindrome")
else:
    print("The string" , string, " is not palindrome")