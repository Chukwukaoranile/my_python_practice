numbers = [12, 24, 45, 32, 12, 12, 32, 23, 24, 12]
dup = []
for num in numbers:
    if num not in dup:
        dup.append(num)
print(dup)
