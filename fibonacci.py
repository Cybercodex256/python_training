def fibonacci(n):
  sequence= [1,2]
  while len(sequence)<n:
     next_number=sequence[-1]+sequence[-2]
     sequence.append(next_number)
     
  print(sequence)

fibonacci(15)
