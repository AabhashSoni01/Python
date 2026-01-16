# Majority Element - More Than n/3
class Solution:
    def findMajority(self, arr):
        n = len(arr)

        cand1 = cand2 = 0
        count1 = count2 = 0

        for num in arr:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = count2 = 0
        for num in arr:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1

        result = []
        if count1 > n // 3:
            result.append(cand1)
        if count2 > n // 3:
            result.append(cand2)

        result.sort()

        return result

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements: ").split()))

obj = Solution()
ans = obj.findMajority(arr)
print("Majority elements (> n/3):", ans)