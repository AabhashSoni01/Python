# 1. Read the input numbers as strings (to easily reverse them).
# 2. Define a helper function to reverse a string and convert it to an integer (which automatically handles the removal of trailing zeros, like "001" becoming 1).
# 3. Calculate the original numbers, sum them, and then reverse the final sum.

def reverse_and_convert(n_str: str) -> int:
    reversed_str = n_str[::-1]

    return int(reversed_str)

def solve():
    try:
        N = int(input())
    except EOFError:
        return
    except ValueError:
        print("Invalid input for number of cases.")
        return

    for _ in range(N):
        try:
            line = input().split()
            if len(line) < 2:
                continue

            A_rev_str = line[0]
            B_rev_str = line[1]
            
        except EOFError:
            break

        A_orig = reverse_and_convert(A_rev_str)
        B_orig = reverse_and_convert(B_rev_str)

        S = A_orig + B_orig
        S_rev = reverse_and_convert(str(S))
        
        print(S_rev)

if __name__ == "__main__":
    solve()