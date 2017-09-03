def format(unformated):
    return ''.join([c for c in unformated if c.isalpha() or c.isspace()])

inputs = []

with open('jvs_500.txt') as examp:
    for line in examp:
        unit = line.split(",")
        inputs.append(unit[7])
examp.closed

with open('in', 'a') as inp:
    for i in range(0,len(inputs)):
        if inputs[i]:
           inp.write(","+format(inputs[i]))
inp.closed