from ft_len_num import ft_len_num


def ft_rev_num(a):
    k = ft_len_num(a)
    s = k
    o = 0
    c = a
    for i in range(k):
        o += (c % 10) * 10 ** s
        c //= 10
        s -= 10
    return o // 10
