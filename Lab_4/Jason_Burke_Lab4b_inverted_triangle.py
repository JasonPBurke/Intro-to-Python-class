#Display an inverted triangle drawn with stars

for row in range(11, 0, -1):
    for col in range(row - 1):
        print('*', end='')
    print()

end = input("press any key to end")
