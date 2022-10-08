n = int(input()).bit_length()-1
a = 1
for i in range(n):
    a *= 2

print(n, a)
