import random
import requests


def getHeaders():
    user_agents = ['Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                   'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) '
                   'Version/5.1 Safari/534.50',
                   'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11']
    headers = {'User-Agent': random.choice(user_agents)}
    return headers


url = 'https://httpbin.org/headers'
url = 'https://httpbin.org/ip'
proxies = {'http': '120.236.128.201:8060'}
# proxies = {'http': 'http://114.99.54.65:8118'}
strhtml = requests.get(url, headers=getHeaders(), proxies=proxies)
print(strhtml.text)
