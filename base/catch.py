# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


class BaseRequests:
    useragent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ' \
                r'(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update({'User-Agent': self.useragent,
                               'Accept-Language': 'zh-CN'})

    # 设置请求头
    def set_headers(self, useragent):
        self.s.headers.update({'User-Agent': useragent})

    # 请求url
    def get_page(self, url, timeout=10):
        try:
            self.r = self.s.get(url, timeout=timeout)
        except:
            return False
        return True

    # 创建bsobj
    def build_bs4(self):
        self.bsobj = BeautifulSoup(self.r.content, 'lxml')

    # 将当前页面保存为图片
    def save_as_gif(self, filename='1.gif'):
        with open(filename, 'wb') as fp:
            fp.write(self.r.content)

    # 将当前页面保存为html
    def save_as_html(self, filename='1.html', encoding=None):
        with open(filename, 'w', encoding=encoding) as fp:
            fp.write(self.r.text)


if __name__ == '__main__':
    a = BaseRequests()
    a.get_page(r'https://www.baidu.com')
    a.build_bs4()
    print(a.bsobj.title)
    a.save_as_html(encoding='utf-8')
