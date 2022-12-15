import random
passLength = int(input("Enter password length: "))
p = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
s= "".join(random.sample(p,passLength))
print(s)