def ft_second_simple_max_num(a):
    m = -1
    n = -1
    while a:
        temp = a % 10
        if temp > m:
            n = m
            m = temp
        elif temp > n:
            n = temp
        a = a // 10
        if m == n:
            n = -1
    return n
