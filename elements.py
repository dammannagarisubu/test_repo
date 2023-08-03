my_list = ['41', 'DHRUVA', 'GURU', '13', 'ZARA']
output = ''
for item in my_list:
    if item.isdigit():
        output += item *3
    else:
        output += item + '#'
print([output])