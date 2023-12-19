def name(first_name, last_name,middle_name='io'):
    full_name = f'{first_name} {middle_name} {last_name}'
    return full_name.title()
lab = name('he','jia','jk')
print(lab)