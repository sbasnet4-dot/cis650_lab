def bark (prompt):
    return f'woff!{prompt}'
function = [bark, str.lower, str.capitalize]
print(function[0]('solo'))
print(function[1]('abcd'))
print(function[2]('aaluwa'))