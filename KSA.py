s = []
for x in range(256):
    s.append(x)
kunci = "saputra1"
k = list(kunci)
j = 0
for i in range(256):
    j = (j + s[i] + ord(k[i % len(kunci)])) % 256
    s[i], s[j] = s[j], s[i]
print(s)
