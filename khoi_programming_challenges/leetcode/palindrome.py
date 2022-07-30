

number = 131

# def is_palindrome(number):
#     if number < 10:
#         return True
#     elif (number % 11) == 0:
#         return True 
#     else:
#         return False





def is_palindrome(number):
    if number < 0:
        return False
    sum = 0
    temp = number
    while(int(number) != 0):
        n = int(number % 10)
        print(f"[*] n: {n}")
        sum = (sum*10) + n
        print(f"[*] sum: {sum}")
        number //= 10
        print(f"[*] number: {number}")
        
    if (temp == sum):
        return True
    else:
        return False
    
print(is_palindrome(131))