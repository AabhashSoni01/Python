# Reads T test cases, and for each case,
# calculates and prints the GCD and LCM of two numbers.

import sys
import math

def solve():
    try:
        T_line = sys.stdin.readline()
        if not T_line:
            return

        T = int(T_line)
        
        results = []

        for _ in range(T):
            line = sys.stdin.readline()
            if not line:
                break

            X, Y = map(int, line.split())

            g = math.gcd(X, Y)

            if g == 0:
                l = 0
            else:
                l = (X * Y) // g

            results.append(f"{g} {l}")

        print("\n".join(results))

    except ValueError:
        pass
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    solve()