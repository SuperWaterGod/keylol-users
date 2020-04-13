# coding:utf-8
import csv
import requests
import re
from bs4 import BeautifulSoup
import string
import time
import random


def getTime():
    print("[", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "]", end=" ")


def removeChinese(file):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    english = re.sub(pattern, ' ', file)
    return english


def writeCsv(csvList):
    f = open('keylol.csv', 'a+', newline='')
    writer = csv.writer(f)
    for i in csvList:
        writer.writerow(i)
    f.close()


def getHeaders():
    user_agents = ['Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                   'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) '
                   'Version/5.1 Safari/534.50',
                   'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11']
    headers = {'User-Agent': random.choice(user_agents)}
    return headers


def getHTMLText(uid):
    url = 'https://keylol.com/suid-' + str(uid)
    # proxies = {'http': 'http://114.99.54.65:8118'}
    try:
        r = requests.get(url, timeout=3, headers=getHeaders())
        return r.text
    except:
        return "ERROR"


def operateHTML(text, uid):
    bs = BeautifulSoup(text, "html.parser")
    txt = bs.find_all(class_='pf_l')
    a = removeChinese(txt[2].get_text()).replace("  ", '')
    b = ' '.join(removeChinese(txt[3].get_text()).split())
    strList1 = a.split(' ')
    # 在线时间  注册时间
    strList1[0] = strList1[0].replace('\n', '').replace('\r', '')

    # 积分 体力 蒸汽 动力
    strList2 = b.split(' ')

    # 好友 回帖 主题
    txt = bs.find_all(class_='cl bbda pbm mbm')
    c = ' '.join(removeChinese(txt[0].get_text().translate(str.maketrans('', '', string.punctuation))).split())
    strList3 = c.split(' ')

    getTime()
    print('uid:', uid, strList1[0], strList1[1], strList2[2], strList2[3], strList2[4], strList2[5], strList3[0],
          strList3[1], strList3[2])
    csvList = [(uid, strList1[0], strList1[1], strList2[2], strList2[3], strList2[4],
                strList2[5], strList3[0],
                strList3[1], strList3[2])]
    writeCsv(csvList)


def testError(text, uid):
    bs = BeautifulSoup(text, "html.parser")
    errorTxt = bs.find_all(class_='alert_error')
    if errorTxt:
        losingERROR(uid)
    else:
        txt = bs.find_all(class_='pf_l')
        if not txt[1].get_text():
            nullERROR(uid)
        else:
            a = removeChinese(txt[2].get_text()).replace("  ", '')
            strList1 = a.split(' ')
            strList1[0] = strList1[0].replace('\n', '').replace('\r', '')
            result = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", strList1[0])
            if result:
                inactiveERROR(uid)
            else:
                return "OK"


def overtimeERROR(uid):
    getTime()
    print("uid:", uid, "获取超时")
    f = open('overtime.csv', 'a+', newline='')
    writer = csv.writer(f)
    errorList = [uid]
    writer.writerow(errorList)
    f.close()


def losingERROR(uid):
    getTime()
    print("uid:", uid, "不存在")
    f = open('losing.csv', 'a+', newline='')
    writer = csv.writer(f)
    errorList = [uid]
    writer.writerow(errorList)
    f.close()


def nullERROR(uid):
    getTime()
    print("uid:", uid, "空账号")
    f = open('null.csv', 'a+', newline='')
    writer = csv.writer(f)
    errorList = [uid]
    writer.writerow(errorList)
    f.close()


def inactiveERROR(uid):
    getTime()
    print("uid:", uid, "不活跃账号")
    f = open('inactive.csv', 'a+', newline='')
    writer = csv.writer(f)
    errorList = [uid]
    writer.writerow(errorList)
    f.close()


def loadNum():
    with open("./keylol.csv") as csvFile:
        targetLine = csvFile.readlines()[-1]
        a = int(targetLine.split(',')[0])
    with open("./null.csv") as csvFile:
        targetLine = csvFile.readlines()[-1]
        b = int(targetLine.split(',')[0])
        if a < b:
            a = b
    with open("./inactive.csv") as csvFile:
        targetLine = csvFile.readlines()[-1]
        b = int(targetLine.split(',')[0])
        if a < b:
            a = b
    with open("./overtime.csv") as csvFile:
        targetLine = csvFile.readlines()[-1]
        b = int(targetLine.split(',')[0])
        if a < b:
            a = b
    return a


def main():
    # startUrl = 1
    startUrl = int(loadNum())+1
    endUrl = 336429
    uid = startUrl
    while 1:
        try:
            if getHTMLText(uid) != "ERROR":
                if testError(getHTMLText(uid), uid) == "OK":
                    operateHTML(getHTMLText(uid), uid)
            else:
                overtimeERROR(uid)
            if uid == endUrl:
                break
            # time.sleep(0.1)
            uid+=1
        except:
            continue


main()
print("第一阶段完成")
while 1:
    pass
