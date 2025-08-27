largest = -99
while True:
    Next_Input = int(input('Enter a number or -1 to stop'))
    if Next_Input == -1:
        break
    else:
        if Next_Input > largest :
            largest = Next_Input
print('The largest number is', largest)