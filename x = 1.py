x = 1 
y = 0

# Bitwise AND
print("x & y =", x & y)  # 1 & 0 = 0

# Bitwise OR
print("x | y =", x | y)  # 1 | 0 = 1

# Bitwise XOR
print("x ^ y =", x ^ y)  # 1 ^ 0 = 1

# Bitwise NOT
print("~x =", ~x)  # ~1 = -(1 + 1) = -2

# Additional examples
a = 5  # Binary: 0101
b = 3  # Binary: 0011

# Bitwise AND
print("a & b =", a & b)  # 0101 & 0011 = 0001 (1)

# Bitwise OR
print("a | b =", a | b)  # 0101 | 0011 = 0111 (7)

# Bitwise XOR
print("a ^ b =", a ^ b)  # 0101 ^ 0011 = 0110 (6)

# Bitwise NOT
print("~a =", ~a)  # ~0101 = -(0101 + 1) = -6

# Left shift
print("a << 1 =", a << 1)  # 0101 << 1 = 1010 (10)

# Right shift
print("a >> 1 =", a >> 1)  # 0101 >> 1 = 0010 (2)

# Explanation of ~x
# The bitwise NOT (~) inverts all the bits of the number.
# For example, ~1 flips the bits of 1 (0001 in binary) to 1110,
# which is the two's complement representation of -2.