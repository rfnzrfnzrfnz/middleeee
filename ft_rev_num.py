def ft_rev_num(a):
    c = a % 10
    b = a // 10
    n = a // 100
    k = b % 10
    ft_rev_num = str(c) + str(k) + str(n)
    return ft_rev_num
