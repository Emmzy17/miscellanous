def set_nth_bit(x:int, n:int):
    print(bin(x | 1 << n)[2:])
    return x | 1 << n

print(set_nth_bit(11, 2))