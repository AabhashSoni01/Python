# Reads N, X, and then N skill levels.
# Prints "YES" if skill >= X, otherwise "NO".

import sys

def solve():
    try:
        N_line = sys.stdin.readline()
        if not N_line:
            return
        N = int(N_line)

        X_line = sys.stdin.readline()
        if not X_line:
            return
        X = int(X_line)
        
        results = []

        for _ in range(N):

            Y_line = sys.stdin.readline()
            
            if not Y_line:
                break
            Y = int(Y_line)
   
            if Y >= X:
                results.append("YES")
            else:
                results.append("NO")
        
        print("\n".join(results))

    except ValueError:
        pass
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    solve()