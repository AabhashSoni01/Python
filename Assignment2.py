# Given three numbers find the maximum of three numbers using the ternary operator.

a = 15
b = 25
c = 10

maximum_correct = a if a >= b and a >= c else (b if b >= c else c)

print(f"The numbers are: a = {a}, b = {b}, c = {c}")
print(f"The maximum number is: {maximum_correct}")