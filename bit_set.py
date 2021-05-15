def is_nth_bit_set(x :int, n :int):
    if x & (1 << n):
        return True
    return False

print(is_nth_bit_set(6, 2))