# Consider int val=0xCAFE; Write expressions using bitwise operators that do the following:
# 1. test if at least three of last four bits (LSB) are on
# 2. reverse the byte order (i.e., produce val=0xFECA)
# 3. rotate four bits (i.e., produce val=0xECAF)

import math

VAL = 0xCAFE

print(f"Original Value (Decimal): {VAL}")
print(f"Original Value (Hex):     {hex(VAL)}")
print(f"Original Value (Binary):  {VAL:016b}\n")
print("")

ISOLATED_LSBS = VAL & 0xF

lsb_test_result = bin(ISOLATED_LSBS).count('1') >= 3

print("1. Test if at least three of the last four bits are on:")
print(f"   - Isolated LSBs (Binary): {ISOLATED_LSBS:04b}")
print(f"   - Result (True/False):    {lsb_test_result}")
print("")

reversed_val = ((VAL & 0x00FF) << 8) | ((VAL & 0xFF00) >> 8)

print("2. Reverse the byte order (0xCAFE -> 0xFECA):")
print(f"   - Result (Hex):         {hex(reversed_val)}")
print(f"   - Result (Binary):      {reversed_val:016b}")
print("")

rotated_val = (VAL >> 4) | ((VAL & 0x000F) << 12)

print("3. Rotate four bits right (0xCAFE -> 0xECAF):")
print(f"   - Result (Hex):         {hex(rotated_val)}")
print(f"   - Result (Binary):      {rotated_val:016b}")
print("")