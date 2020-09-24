def ft_covert_num(n, c):
    b = ''
    while n > 0:
        b = str(n % c) + b
        n = n // c
    return b
