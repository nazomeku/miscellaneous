def int_to_bin(num):
    """Take integer and convert it to binary."""
    if num < 0:
        neg = True
        num = abs(num)
    else:
        neg = False
    result = ''
    if num == 0:
        result = '0'
    while num > 0:
        result = str(num % 2) + result
        num = num // 2
    if neg:
        result = '-' + result
    return result
