def ft_sum_num(a):
    result = 1
    while a > 0:
        result += a % 10
        a //= 10
    return result

print(ft_sum_num(123))