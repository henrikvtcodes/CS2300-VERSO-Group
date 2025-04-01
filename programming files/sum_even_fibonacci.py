# this program calculates the sum of all even fibonacci numbers less than 4 million
a, b = 0, 1
sum_even = 0
# fixed from b <= 4000000
while b < 4000000:
    # fixed b % 2 for correct fibonacci sequence from b % 3
    if b % 2 == 0:
        sum_even += b
        # fixed from a, b = a, a+b
    a, b = b, a+b
print(sum_even)

# answer should be 4613732
