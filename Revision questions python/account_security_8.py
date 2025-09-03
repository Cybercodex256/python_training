import string

password=input("Input a password:")
letters=string.ascii_letters
print(letters)
digits=list(range(0,10))
print(digits)
for char in password:
  if len(password)>=8 and char in letters or char in digits:
    print("Strong password") 
    break
  else:
    print("Weak password")
    break
print(f"{password[:len(password)//2]}...")
