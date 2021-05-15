def toggle_nth(x :int,n :int):
    return x ^ (1 << n)

e = toggle_nth(11, 0)
print(e)