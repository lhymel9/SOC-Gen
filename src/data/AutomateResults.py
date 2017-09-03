edited = []
with open('out') as out:
    for line in out:
        unit = line.split(",")
        print(unit[0] + " vs " + unit[2])
        judge = input()
        if judge == 'q':
            unit.append('pass')
        elif judge == 'w':
            unit.append('fail')
        elif judge == 'a':
            unit.append('Result')
        else:
            unit.append('uncertain')
        edited.append(",".join(unit.rstrip()))
out.closed

with open('results', 'a') as res:
    for line in edited:
        res.write(line+'\n')
res.closed
