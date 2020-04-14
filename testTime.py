import time


def getTime():
    print("[", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "]", end=" ")


start = time.perf_counter()
string = "12312121312"
print("[", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "]", string)
time.sleep(3)
getTime()
end = time.perf_counter()
print(str(end - start))

