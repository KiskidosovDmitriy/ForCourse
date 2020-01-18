def pts(line):
    return line.replace(',', " ").replace('.', " ")


def dsts(line):
    return line.replace('  ', " ")


def low(line):
    return line.lower()


if __name__ == '__main__':
    f = open('data.txt', 'r')
    out = open('output.txt', 'w')
    line = f.readline()
    for line in f:
        line = pts(line)
        line = dsts(line)
        line = low(line)
        out.write(line)

    f.close()
    out.close()

