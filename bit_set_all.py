def set_all_bit(x: int):
    for i in range(len(bin(x)[2:])):
        x = x | (1 << i)
    print(bin(x)[2:])
    return x
        
print(set_all_bit(112))
