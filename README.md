# keylol-users  获取keylol门户网站用户数据
#### 主要爬取了 UID,在线时间,注册时间,积分,体力,蒸汽,动力,好友,回帖,主题  数据
#### 汇总结果已在[keylol](https://keylol.com/t582817-1-1)发布

## Python文件说明
***
* keylol.py
> 主程序
* TEST.py
> 测试所有函数是否正常
* testCls.py
> 测试清屏
* testCsv.py
> 测试csv文件读写
* testError.py
> 测试错误判断
* testHeaders.py
> 测试随机headers
* testInactive.py
> 测试不活跃用户判断
* testLoad.py
> 测试获取上次读取的最后一个UID
* testOvertime.py
> 测试超时连接
* testTime.py
> 测试显示系统时间
## HTML文件说明
***
* error.html
> losing用户
* error1.html
> null用户
* error2.html
> inactive用户
* error3.html
> inactive用户
* test.html
> 本地测试使用静态网页
## ERROR用户说明
***
* incative
> 用户不活跃，部分数据丢失
* null
> 用户太久没登录，系统自动归档
* losing
> 该uid不存在
* overtime
> 连接超时
