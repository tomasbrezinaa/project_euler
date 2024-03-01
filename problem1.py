def sum_divisible_by(value,target=1000):
    p = (target-1) // value
    return value*(p*(p+1)) // 2

output = sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)
print(output)