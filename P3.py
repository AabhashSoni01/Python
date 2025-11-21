def arithmetic_series(n):
    a= 5
    d = 3
    nth_term = a + (n - 1) * d
    sum= (n / 2) * (2 * a + (n - 1) * d)
    
    return nth_term, sum  

n = int(input("Enter the value of n: "))
nth_term, sum = arithmetic_series(n)  
print(f"The nth term is: {nth_term}")
print(f"The sum is: {sum}")