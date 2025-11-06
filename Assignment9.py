# Reads N test cases and finds the package size A
# that maximizes the number of leftover lemon cakes.

import sys

def solve():
    try:
        T = int(sys.stdin.readline())
        
        results = []
        for _ in range(T):
            N = int(sys.stdin.readline())          
            optimal_A = (N // 2) + 1       
            results.append(str(optimal_A))          
        print("\n".join(results))

    except EOFError:
        pass
    except ValueError:
        pass
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    solve()