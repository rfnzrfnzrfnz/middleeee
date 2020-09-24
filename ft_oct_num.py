def ft_oct_num(n):
    b = ''
    while n > 0:
        b = str(n % 8) + b
        n = n // 8
    return b


