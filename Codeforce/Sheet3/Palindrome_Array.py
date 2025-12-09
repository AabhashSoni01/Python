n = int(input())
arr = list(map(int, input().split()))
rev = arr[::-1]
print("YES" if arr == rev else "NO")