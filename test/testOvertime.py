import numpy as np

with open('./overtime.csv', encoding='gb18030') as f:
    data = np.loadtxt(f, str, delimiter=",", usecols=(0, 0))
a = 0.0
for i in range(0, len(data[:-1, 0])):
    print(data[i, 0])
print("超时一共：")
print(len(data[:-1, 0]) + 1)
