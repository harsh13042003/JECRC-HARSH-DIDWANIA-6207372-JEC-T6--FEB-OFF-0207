file = open('temp.txt', 'w')
file.write('popiuydsdfgh[jhgfd]\n')
file.writelines([
    'first line\n',
    'second line\n',
    'third line\n'
])
file.close()
