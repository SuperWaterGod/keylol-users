# coding:utf-8
import csv
a="测试1"
b="测试2"
c="测试3"
string = [(a, b, c)]

data = [
    ("测试1", '软件测试工程师'),
    ("测试2", '软件测试工程师'),
    ("测试3", '软件测试工程师'),
    ("测试4", '软件测试工程师'),
]
f = open('222.csv', 'a+', newline='')
writer = csv.writer(f)
for i in string:
    writer.writerow(i)
f.close()
