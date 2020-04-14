# keylol-users  获取keylol门户网站用户数据
#### 主要爬取了 UID,在线时间,注册时间,积分,体力,蒸汽,动力,好友,回帖,主题  数据
#### 汇总结果已在[keylol](https://keylol.com/t582817-1-1)发布

## 文件说明
***
* __keylol.py__
> __主程序__
* HTML
>测试使用的或者有问题的静态页面
* test
> 测试各种功能
* data
> 简单数据处理结果

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
