#Display an inverted triangle

for row in range(11, 0, -1):
    for col in range(row - 1):
        print('*', end='')
    print()
