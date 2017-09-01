from run import run_main

with open('in') as f:
    keywords = f.read()
f.closed

keywords = keywords.split(',')

results = []
for kw in keywords:
    industry = kw[:2]
    search = kw[2:]
    results.append(run_main(search, industry))

with open('out', 'w') as out:
    for result in results:
        out.write(result + '\n')
out.closed