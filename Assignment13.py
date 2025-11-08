# Simulates the stone-placing game to find the winner.

import sys

def solve():
    try:
        N_line = sys.stdin.readline()
        if not N_line:
            return
        
        remaining_stones = int(N_line.strip())
        
        current_round = 1
        winner = ""

        while True:
            stones_ramesh_puts = current_round
            
            if remaining_stones <= stones_ramesh_puts:
                winner = "Ramesh"
                break
            
            remaining_stones -= stones_ramesh_puts
            
            stones_suresh_puts = current_round * 2
            
            if remaining_stones <= stones_suresh_puts:
                winner = "Suresh"
                break
                
            remaining_stones -= stones_suresh_puts
            
            current_round += 1
            
        print(winner)

    except ValueError:
        pass
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    solve()