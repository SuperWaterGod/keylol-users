# coding:utf-8
import csv
import requests  # 导入requests包
import re
from bs4 import BeautifulSoup
import string
import time


def find_english(file):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    english = re.sub(pattern, ' ', file)
    return english


head = {
    'User-Agent': 'BiLiBiLi WP Client/1.0.0 (orz@loli.my)',
}
url = 'https://keylol.com/suid-278578'

start = time.perf_counter()
'''
f = open('./error4.html', mode='r', encoding='utf-8')
bs = BeautifulSoup(f, "html.parser")
'''
strhtml = requests.get(url, headers=head)
# print(strhtml.text)
bs = BeautifulSoup(strhtml.text, "html.parser")
# print(f.read())

txt = bs.find_all(class_='pf_l')
print(txt)
print("--------------------------------------------------")
print(find_english(txt[2].get_text()))
print(find_english(txt[3].get_text()))
a = find_english(txt[2].get_text()).replace("  ", '')
b = ' '.join(find_english(txt[3].get_text()).split())
strlist1 = a.split(' ')
strlist1[0] = strlist1[0].replace('\n', '').replace('\r', '')
'''print("在线时间" + str(strlist1[0]))  # 在线时间
print("注册时间" + str(strlist1[1]))  # 注册时间
'''
'''for value in strlist1:
    print(value)'''
# print("--------------------------------------------------")
strlist2 = b.split(' ')
'''print('积分' + str(strlist2[2]))  # 积分
print('体力' + str(strlist2[3]))  # 体力
print('蒸汽' + str(strlist2[4]))  # 蒸汽
print('动力' + str(strlist2[5]))  # 动力'''
'''for value in strlist2:
    print(value)'''
# print("--------------------------------------------------")

inf = bs.find_all(class_='cl bbda pbm mbm')
# print(find_english(inf[0].get_text().translate(str.maketrans('', '', string.punctuation))))
c = ' '.join(find_english(inf[0].get_text().translate(str.maketrans('', '', string.punctuation))).split())
strlist3 = c.split(' ')
'''print('好友' + str(strlist3[0]))  # 好友
print('回帖' + str(strlist3[1]))  # 回帖
print('主题' + str(strlist3[2]))  # 主题'''
'''
for value in strlist3:
    print(value)'''

csvname = [("UID", "在线时间", "注册时间", "积分", "体力", "蒸汽", "动力", "好友", "回帖", "主题")]
csvlist = [('uid', strlist1[0], strlist1[1], strlist2[2], strlist2[3], strlist2[4],
            strlist2[5], strlist3[0],
            strlist3[1], strlist3[2])]

f = open('test.csv', 'a+', newline='')
writer = csv.writer(f)

for i in csvlist:
    writer.writerow(i)
f.close()

print("[", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "]", 'uid', strlist1[0], strlist1[1], strlist2[2],
      strlist2[3], strlist2[4],
      strlist2[5], strlist3[0],
      strlist3[1], strlist3[2])

time.sleep(0.98)
end = time.perf_counter()
print(str(end - start))
