a, b = 1, 1
sum_even = 0
while b <= 4000000:
    if b % 3 == 0:
        sum_even += b
    a, b = a, a+b
print(sum_even)

# answer should be 4613732
