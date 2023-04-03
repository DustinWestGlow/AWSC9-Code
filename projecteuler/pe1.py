# FIRST EDIT
a = 123
print(a)
# TRY IT 
limit = 10**3
total = 0

for i in range(1, limit):
    if (i % 3 == 0) or (i % 5 == 0):
        total += i

print(total)