def sort_pair(x, y):
    (x, y) = (x, y)
    if x > y:
        (x, y) = (y, x)
    return


print(sort_pair(5, 2))
