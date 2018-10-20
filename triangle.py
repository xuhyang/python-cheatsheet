size = int(input("Enter a number: "))
mid = size // 2
left_edge = right_edge = mid
col = size
numRows = mid + 1
for i in range(0, numRows):

    for j in range(0, col):

        if i == (numRows - 1) or j == left_edge or j == right_edge :
            print('*', end='')
        else:
            print(' ', end='')

    print()
    left_edge -= 1
    right_edge += 1



