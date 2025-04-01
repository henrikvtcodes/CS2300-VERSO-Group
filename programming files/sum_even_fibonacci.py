# this program calculates the sum of all even fibonacci numbers less than 4 million
a, b = 0, 1
sum_even = 0
while b <= 4000000:
    if b % 3 == 0:
        sum_even += b
    a, b = a, a+b
print(sum_even)

# answer should be 4613732
