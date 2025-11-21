val = 0xCAFE

last_four_bits = val & 0xF

rev_byte = (val >> 8) | (val << 8)

if last_four_bits >= 0xE:
    print("at least three of the last four bits (LSB) are ON")

print(f"Reversed byte value:", hex((rev_byte & 0xFFFF)))