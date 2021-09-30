import csv
with open("table.csv") as f:
    a = [l[0].split(";") for l in csv.reader(f)]
    
a = [i[:len(i)//2] + [0] + i[len(i)//2:] for i in a]
a = a[:len(a)//2] + [[0]*len(a[0])] + a[len(a)//2:]
 
with open("answ4.csv", "w") as f:
    w = csv.writer(f)
    for l in a:
        w.writerow(l)


