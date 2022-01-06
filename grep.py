import re
file = open(input('Input the name of the file you wanna open: '))
times = 0
for line in file:
    #line = line.rstrip()
    x = re.findall('^emjay', line)
    times +=len(x)
print('Emjay appeared %s times' % times)