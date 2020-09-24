def ft_second_simple_max_num(a):
    q = 0
    w = 0
    e = a
    while e > 0:
        if q < e % 10:
            q = e % 10
        e //= 10
    while a > 0:
        if q >= w < a % 10:
            w = a % 10
        a //= 10

    if w == q:
        return -1
