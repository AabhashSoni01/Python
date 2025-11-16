days = int(input())
y = days // 365
m = (days % 365) // 30
d = (days % 365) % 30
print(f"{y} years")
print(f"{m} months")
print(f"{d} days")