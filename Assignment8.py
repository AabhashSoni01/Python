# Reads N test cases and computes the last digit of a^b.

import sys

def solve():
    try:
        N = int(sys.stdin.readline())
        
        results = []
        for _ in range(N):
            a, b = map(int, sys.stdin.readline().split())
            
            last_digit = pow(a, b, 10)
            
            results.append(str(last_digit))
            
        print("\n".join(results))

    except EOFError:
        pass
    except ValueError:
        pass
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    solve()