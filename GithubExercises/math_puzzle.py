#selected two numbers 10 and 4
base=10
exponent=4

#Calculated using the power
ans=base**exponent
print(f"Power Answer: {ans}")

#Third nunber
large_number = 15

#Finding quotient
quotient=large_number//base
print(f"Quotient: {quotient}")

exact_result=large_number/base
print(f"Exact result:{exact_result}")


final_value=ans+quotient+exact_result
print(f"Final value: {final_value}")
print(f"The final value is of type:{type(final_value)}")



