# Calculates the minimum number of notes required for a given amount,
# starting from a specified denomination and going down to 1.
# The logic iteratively checks the largest possible denomination first (a greedy approach).

def calculate_notes_required(amount: int, start_denomination: int):
    ALL_DENOMINATIONS = [100, 50, 20, 10, 5, 2, 1]
    
    notes_count = {}
    remaining_amount = amount
    
    try:
        start_index = ALL_DENOMINATIONS.index(start_denomination)
    except ValueError:
        print(f"Error: Starting denomination {start_denomination} is not supported.")
        return notes_count

    denominations_to_use = ALL_DENOMINATIONS[start_index:]

    print(f"\n--- Calculating Notes for Amount {amount} (Starting from {start_denomination}) ---")

    for denom in denominations_to_use:
        if remaining_amount >= denom:
            count = remaining_amount // denom
            remaining_amount %= denom
            
            notes_count[denom] = count
            
        else:
            notes_count[denom] = 0
        
    return notes_count

def solve():
    try:
        amount_input = input()
        denomination_input = input()
        
        amount = int(amount_input)
        start_denomination = int(denomination_input)
        
        if amount <= 0:
            print("Error: Amount must be a positive integer.")
            return

    except EOFError:
        return
    except ValueError:
        print("Error: Input must be valid integers.")
        return
    
    result = calculate_notes_required(amount, start_denomination)
    
    if result:
        print("\nOutput:")
        for denom, count in result.items():
            print(f"{denom} rupees note: {count}")

# Execute the main function
if __name__ == "__main__":
    
    print("--- Running with Sample Input: 748 and 50 ---")
    
    sample_amount = 748
    sample_denom = 50
    sample_result = calculate_notes_required(sample_amount, sample_denom)
    
    print("\nSample Output:")
    for denom, count in sample_result.items():
        print(f"{denom} rupees note: {count}")