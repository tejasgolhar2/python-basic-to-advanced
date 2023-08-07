names = ['John', 'Edy', 'Jane', 'Kane']
scores = [90, 95, 80, 75]

print("{a:<10} {b:<5}".format(a="Name",b="Score"))
# print("{0:<10} {1:<5}".format(0 ="Name",1 ="Score"))

for i in range(0,len(names)):
    name = names[i]
    score = scores[i]
    print("{:<10} {:<5}".format(name,score))

