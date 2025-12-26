import sys

def solve():
    counts = [0] * 26
    sys.stdin.readline()
    
    while True:
        part = sys.stdin.read(65536)
        if not part:
            break
            
        for char in part:
            code = ord(char)
            if 97 <= code <= 122:
                counts[code - 97] += 1

    output = []
    for i in range(26):
        if counts[i] > 0:
            sys.stdout.write(chr(i + 97) * counts[i])

if __name__ == "__main__":
    solve()