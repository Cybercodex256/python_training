"""Exercise: 19: Print Alternate Prime Numbers till 20
A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11)."""
numbers = list(range(1,20))
print(numbers)
ans =[]
def isPrime(num):
   for z in range(1,num):
    dividers=[i for i in range(1,num**2) if num%i == 0]
    if len(dividers)==2:
      ans.append(num)
   return  ans

print(isPrime(20))

