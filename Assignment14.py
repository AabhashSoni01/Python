# Prints a staircase of '#' symbols of height n.
# Args: n (int): The number of levels for the staircase.

import sys

def print_staircase(n):
    for i in range(1, n + 1):
        level = "#" * i
        print(level)

def main():
    try:
        n_line = sys.stdin.readline()
        if not n_line:
            return
            
        N = int(n_line.strip())
        
        print_staircase(N)

    except ValueError:
        print("Error: Input must be an integer.", file=sys.stderr)
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()