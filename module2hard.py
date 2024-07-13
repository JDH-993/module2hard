n = int(input())
k = ''
result = ''
for i in range(3, n + 1):
    if n % i == 0:
        for g in range(1, i + 1):
            h = i - g
            p = int(g)
            if n % (h + g) == 0 and h != 0 and h > g >= p:
                k = k + " " + str(g) + str(h)

for e in range(1, 10):
    for j in range(len(k)):
        if k[j] == " " and k[j + 1] == str(e):
            w = (j+1).__index__()
            for d in range(w, len(k)):
                if k[d] == " ":
                    break
                else:
                    result = result + k[d]
print(result)

