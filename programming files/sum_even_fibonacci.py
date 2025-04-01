a, b = 1, 1  # Changed initial values
sum_even = 0
while b <= 4000000:  # Changed to <= which will cause one extra iteration
    if b % 3 == 0:  # Changed from checking for even to divisible by 3
        sum_even += b
    a, b = a, a+b  # Incorrect Fibonacci sequence update
print(sum_even)

# answer should be 4613732
