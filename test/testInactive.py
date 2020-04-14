import re
from datetime import datetime

test_date = '他的生日是 14:34,是个可爱的小宝贝.二宝的生日是 11:34,好可爱的.'

# date
mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", test_date)
if mat:
    print("存在时间")
else:
    print("不存在")
