def ft_mirror_num(num):
    while num:
        l = num % 10
        f = 0
        while num:
            if num // 10 > 0:
                num = num // 10
            else:
                f = num
                num = num // 10
        if f != l:
            print("FALSE")
            return ''
    print('TRUE')
    return ''
