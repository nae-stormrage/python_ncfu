import string
import re

j = str(string.ascii_uppercase)
print(len(j))

f = open("data_v2.txt")
s = f.read().strip()
print(len(s))

for i in range(26):
    s = s.replace(j[i],'/')
print(s)

n = len(re.findall('/', s))
print(n)
