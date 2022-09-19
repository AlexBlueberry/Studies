s = []
k = 0
for i in range(120115, 120200+1):
    m = 0
    for j in range(1, i+1):
        if i%j == 0:
            m += 1
    if m > k:
        k = m
    print(i, k)
