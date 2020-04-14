from bs4 import BeautifulSoup
import re


def removeChinese(file):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    english = re.sub(pattern, ' ', file)
    return english


f = open('./error3.html', mode='r', encoding='utf-8')
bs = BeautifulSoup(f, "html.parser")
errortxt = bs.find_all(class_='alert_error')
if errortxt:
    print("错误")
else:
    txt = bs.find_all(class_='pf_l')
    if not txt[1].get_text():
        print("不存在")
    else:
        a = removeChinese(txt[2].get_text()).replace("  ", '')
        strList1 = a.split(' ')
        strList1[0] = strList1[0].replace('\n', '').replace('\r', '')
        mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", strList1[0])
        if mat:
            print("不活跃用户")
        else:
            print("OK")

