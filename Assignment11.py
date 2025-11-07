# Reads N work durations and calculates the total time for each.

import sys

def solve():
    try:
        N_line = sys.stdin.readline()
        if not N_line:
            return
        N = int(N_line)
        
        results = []
        for _ in range(N):
            line = sys.stdin.readline()
            if not line:
                break 
            SH, SM, EH, EM = map(int, line.split())

            start_total_minutes = (SH * 60) + SM
            end_total_minutes = (EH * 60) + EM

            duration_in_minutes = end_total_minutes - start_total_minutes

            duration_hours = duration_in_minutes // 60

            duration_minutes = duration_in_minutes % 60

            results.append(f"{duration_hours} {duration_minutes}")

        print("\n".join(results))

    except ValueError:
        pass
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    solve()