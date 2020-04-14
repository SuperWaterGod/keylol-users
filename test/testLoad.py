# coding=utf8

with open("./keylol.csv") as csvfile:
    targetLine = csvfile.readlines()[-1]
    a=targetLine.split(',')[0]

with open("./null.csv") as csvfile:
    targetLine = csvfile.readlines()[-1]
    b=targetLine.split(',')[0]
    if a<b:
        a=b
with open("./inactive.csv") as csvfile:
    targetLine = csvfile.readlines()[-1]
    b=targetLine.split(',')[0]
    if a<b:
        a=b
with open("./overtime.csv") as csvfile:
    targetLine = csvfile.readlines()[-1]
    b=targetLine.split(',')[0]
    if a<b:
        a=b
print(a)

