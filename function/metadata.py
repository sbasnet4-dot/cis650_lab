def rememeber(x):
    if hasattr(rememeber,'Author'):
     return f'hi {x}. Author by {rememeber.Author}'
    else:
        return f'hi {x}'
print(rememeber('chad'))
i = rememeber
i.Author = 'suddos'
print(rememeber('chad'))

