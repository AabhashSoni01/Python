# Prints the first n rows of Pascal's Triangle.
# Args: n (int): The number of rows to print.

import sys

def print_pascal(n):
    
    if n <= 0:
        return

    row = [1]
    
    for i in range(n):
        print(" ".join(map(str, row)))
        temp_row = [0] + row + [0]
        next_row = []

        for j in range(len(temp_row) - 1):
            next_row.append(temp_row[j] + temp_row[j+1])
            
        row = next_row

def main():
    try:
        print("Enter the number of rows for Pascal's Triangle:")
        n_line = sys.stdin.readline()
        if not n_line:
            return
            
        N = int(n_line.strip())
        
        print("\nResultant Pascal's Triangle:")
        print_pascal(N)

    except ValueError:
        print("Error: Input must be an integer.", file=sys.stderr)
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()