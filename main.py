import string as s
import random as r

letters = s.ascii_letters
dig = s.digits
symobls  = '!@#$%^&*'


def passwd(n):

    for i in range(1,n+1):
        print(r.choice(letters+dig+symobls), end="")

    
n = int(input("Enter length of Password: "))
print("Password is Generate Successfully!")
passwd(n)
