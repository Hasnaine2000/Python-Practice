# Demonstrating bitwise operations in Python

a = 5  # Binary: 0101
b = 3  # Binary: 0011

print("a & b =", a & b)  # AND operation: 0101 & 0011 = 0001 (1)
print("a | b =", a | b)  # OR operation: 0101 | 0011 = 0111 (7)
print("a ^ b =", a ^ b)  # XOR operation: 0101 ^ 0011 = 0110 (6)
print("~a =", ~a)        # NOT operation: ~0101 = -(0101 + 1) = -6
print("a << 1 =", a << 1)  # Left shift: 0101 << 1 = 1010 (10)
print("a >> 1 =", a >> 1)  # Right shift: 0101 >> 1 = 0010 (2)