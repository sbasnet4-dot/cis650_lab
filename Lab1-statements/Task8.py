alphabetical='abcdefghijklmnopqrstuvwxyz'
while True:
    user_entry = input('Enter a letter or blank to exit:')
    if user_entry == '':
        break
    else:
        position = alphabetical.find(user_entry)
        print(f'{user_entry} is at position {position}')



alphabetical='abcdefghijklmnopqrstuvwxyz'
while True:
    user_entry = input('Enter a letter or blank to exit:')
    if user_entry == '':
        break
    else:
        position = alphabetical.find(user_entry)
        if position == -1:
            print(f'{user_entry} is not an alphabetical')
        else:
            print(f'{user_entry} is at position {position}')
