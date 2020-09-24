def ft_bin_num(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b
