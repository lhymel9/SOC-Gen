inputs = []

with open('examples.txt') as examp:
    for line in examp:
        unit = line.split(",")
        inputs.append(unit[2][:2]+unit[7])
examp.closed

with open('in', 'a') as inp:
    for i in range(0,len(inputs)):
        if inputs[i]:
           inp.write(","+inputs[i])
inp.closed