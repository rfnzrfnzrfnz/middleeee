def ft_second_max_num(a):
    m = -1
    c = -1
    while a:
        temp = a % 10
        if temp > m:
            c = m
            m = temp
        elif temp > c:
            c = temp
        a = a // 10
    return c
