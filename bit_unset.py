def unset_nth_bit(x :int, n :int):
    print(bin(x & ~ (1 << n))[2:])
    return x & ~(1 << n)
    

print(unset_nth_bit(6, 1))