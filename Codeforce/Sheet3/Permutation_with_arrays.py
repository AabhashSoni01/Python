n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()

if arr1 == arr2:
    print("yes")
else:
    print("no")