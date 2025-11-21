n = int(input())     
x = int(input())     
skills = []          
for y in range(n):
    skills.append(int(input()))
for skill in skills:
    if skill >= x:
        print("YES")
    else:
        print("NO")