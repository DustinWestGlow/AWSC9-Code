# https://projecteuler.net/problem=1
# Find the sum of all the multiples of 3 or 5 below 1000.
limit = 10**3
total = 0

for i in range(1, limit):
    if (i % 3 == 0) or (i % 5 == 0):
        total += i

print(total)