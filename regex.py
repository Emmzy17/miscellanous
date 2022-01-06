import re
file = open('file.txt')
num = 0
for line in file:
    if re.search('emjay', line):
       num+=1

print(num)
