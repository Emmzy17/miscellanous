def is_even_odd(x :int):
    if x & 1 == 0:
        return "Even"
    return "Odd"

print(is_even_odd(5))
print(is_even_odd(80))
print(is_even_odd('ten'))