while True:
    x = int(input('Please enter a number (''0'' to quit): '))
    if x % 2:
        print('odd')
    else:
        print('even')
    if x == 0:
        break
print('thank you!')
