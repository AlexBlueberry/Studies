s = [i for i in open("ghj.txt")]

counter = 0

for j in s:
    if j.count("E") > j.count("A"):
        counter += 1

print(counter)
