f = open('data.txt', 'r')
out = open('output.txt', 'w')
line = f.readline()


def pts(line):
    return out.write(line.replace(',', " ").replace('.'," "))


def dsts(line):
    return out.write(line.replace('  '," "))


def low(line):
    return out.write(line.lower())


for line in f:
    pts(line)
    dsts(line)
    low(line)

f.close()
out.close()
