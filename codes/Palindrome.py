def is_int_palindrome(number: int) -> bool:
    reverse=0
    n=number
    while number:
        d=number%10
        reverse=reverse*10+d
        number=number//10
    if(n==reverse):
        return True
    else:
        return False
