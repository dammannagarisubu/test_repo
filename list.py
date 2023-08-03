list = [1, 2, 3, 2, 5, 3, 6, 1]
dup = []
for i in set(list):
    if list.count(i) > 1:
        dup.append(i)
print(dup)