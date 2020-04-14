import numpy as np
import csv
from datetime import datetime


# 字符串转为日期时间格式
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))


with open('./keylol.csv', encoding='gb18030') as f:
    data = np.loadtxt(f, str, delimiter=",", skiprows=1, usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
a = 0.0
list = []
for i in range(0, len(data[:-1, 0])):
    # print(data[i, 2])
    update_str = parse_ymd(data[i, 2])
    list.append(int(update_str.year))

for i in set(list):
    print("在{0}年注册的人数为：{1}".format(i, list.count(i)))

# 积分
print("  ")
print("积分")
scoring = 0
for i in range(0, len(data[:-1, 3])):
    if int(data[i, 3]) < 0:
        # print("特殊积分",data[i, 0],data[i, 3])
        continue
    # print(data[i, 3])
    scoring += int(data[i, 3])
print("所有用户总积分：", scoring)
print("平均积分：", scoring / len(data[:-1, 3]))

MemberGroup = [0 for i in range(9)]
MemberGroup_av = [0 for i in range(9)]
Theme_av = [0 for i in range(9)]
Replies_av = [0 for i in range(9)]

for i in range(0, len(data[:-1, 3])):
    # 积分禁封
    if int(data[i, 3]) < 0:
        MemberGroup[0] += 1
        MemberGroup_av[0] += int(data[i, 3])
        Theme_av[0] += int(data[i, 9])
        Replies_av[0] += int(data[i, 8])
    # 初阶会员
    elif 0 <= int(data[i, 3]) < 100:
        MemberGroup[1] += 1
        MemberGroup_av[1] += int(data[i, 3])
        Theme_av[1] += int(data[i, 9])
        Replies_av[1] += int(data[i, 8])
    # 进阶会员
    elif 100 <= int(data[i, 3]) < 500:
        MemberGroup[2] += 1
        MemberGroup_av[2] += int(data[i, 3])
        Theme_av[2] += int(data[i, 9])
        Replies_av[2] += int(data[i, 8])
    # 高阶会员
    elif 500 <= int(data[i, 3]) < 1000:
        MemberGroup[3] += 1
        MemberGroup_av[3] += int(data[i, 3])
        Theme_av[3] += int(data[i, 9])
        Replies_av[3] += int(data[i, 8])
    # 精锐会员
    elif 1000 <= int(data[i, 3]) < 2000:
        MemberGroup[4] += 1
        MemberGroup_av[4] += int(data[i, 3])
        Theme_av[4] += int(data[i, 9])
        Replies_av[4] += int(data[i, 8])
    # 支柱会员
    elif 2000 <= int(data[i, 3]) < 5000:
        MemberGroup[5] += 1
        MemberGroup_av[5] += int(data[i, 3])
        Theme_av[5] += int(data[i, 9])
        Replies_av[5] += int(data[i, 8])
    # 核心会员
    elif 5000 <= int(data[i, 3]) < 10000:
        MemberGroup[6] += 1
        MemberGroup_av[6] += int(data[i, 3])
        Theme_av[6] += int(data[i, 9])
        Replies_av[6] += int(data[i, 8])
    # 旗舰会员
    elif 10000 <= int(data[i, 3]) < 50000:
        MemberGroup[7] += 1
        MemberGroup_av[7] += int(data[i, 3])
        Theme_av[7] += int(data[i, 9])
        Replies_av[7] += int(data[i, 8])
    # 毕业会员
    elif int(data[i, 3]) > 50000:
        MemberGroup[8] += 1
        MemberGroup_av[8] += int(data[i, 3])
        Theme_av[8] += int(data[i, 9])
        Replies_av[8] += int(data[i, 8])
for i in range(9):
    MemberGroup_av[i] /= MemberGroup[i]
    Theme_av[i] /= MemberGroup[i]
    Replies_av[i] /= MemberGroup[i]
print("各个积分组人数", MemberGroup)
print("平均积分", MemberGroup_av)
print("平均主题", Theme_av)
print("平均帖子", Replies_av)

# 体力
print("  ")
print("体力")
Strength = 0
for i in range(0, len(data[:-1, 4])):
    if int(data[i, 4]) < 0 or int(data[i, 4]) > 80000:
        continue
    Strength += int(data[i, 4])
print("所有用户总体力：", Strength)
print("平均体力:", Strength / len(data[:-1, 4]))

# 蒸汽
print("  ")
print("蒸汽")
Steam = 0
for i in range(0, len(data[:-1, 5])):
    if int(data[i, 5]) < 0:
        continue
    Steam += int(data[i, 5])
print("所有用户总蒸汽：", Steam)
print("平均蒸汽:", Steam / len(data[:-1, 5]))

# 动力
print("  ")
print("动力")
Power = 0
for i in range(0, len(data[:-1, 6])):
    if int(data[i, 6]) < 0:
        continue
    Power += int(data[i, 6])
print("所有用户总动力：", Power)
print("平均动力:", Power / len(data[:-1, 6]))

# 好友
print("  ")
print("好友")
Friends = 0
for i in range(0, len(data[:-1, 7])):
    if int(data[i, 7]) < 0:
        continue
    Friends += int(data[i, 7])
print("所有用户总好友：", Friends)
print("平均好友:", Friends / len(data[:-1, 7]))

# 回帖
print("  ")
print("回帖")
Replies = 0
for i in range(0, len(data[:-1, 8])):
    if int(data[i, 8]) < 0:
        continue
    Replies += int(data[i, 8])
print("所有用户总回帖：", Replies)
print("平均回帖:", Replies / len(data[:-1, 8]))

# 主题
print("  ")
print("主题")
Theme = 0
for i in range(0, len(data[:-1, 9])):
    if int(data[i, 9]) < 0:
        continue
    Theme += int(data[i, 9])
print("所有用户总主题：", Theme)
print("平均主题:", Theme / len(data[:-1, 9]))

# 在线时间
print("  ")
print("在线时间")
Time = 0
for i in range(0, len(data[:-1, 1])):
    if int(data[i, 1]) < 0:
        continue
    Time += int(data[i, 1])
print("所有用户总在线时间：", Time)
print("平均在线时间:", Time / len(data[:-1, 1]))

# 勋章
print("  ")
print("勋章")
PSZ = 0
SZ = 4734
for i in range(0, len(data[:-1, 1])):
    if int(data[i, 1]) >= 999:
        if int(data[i, 9]) != 0:
            if int(data[i, 1])/int(data[i, 9]) <= 9.9:
                PSZ += 1
print("片十字花瓣：", PSZ)
print("十字花瓣:", SZ)
