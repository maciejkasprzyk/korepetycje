from sys import stdin

for line in stdin:
    print(repr(line))
    line = line.strip()
    print(repr(line))

