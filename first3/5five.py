import re

inp = input('укажите название файла:\n')
lines = 0
in_file = open(r'C:\projects\seclab\textforlab\''[:-1] + inp + '.txt', mode='r', encoding='utf-8')
out_file = open(r'C:\projects\seclab\textforlab\''[:-1] + inp + '_result.txt', mode='w', encoding='utf-8')
text = in_file.read()

pattern = r'https?:\/\/(?:[-\w]+\.)?([-\w]+\.\w+)(?:\.\w+)?\/?.*'

domen = re.findall(pattern, text)

for item in domen:
    lines += 1
    out_file.write(str(lines) + ')' + item + '\n')

in_file.close()
out_file.close()
