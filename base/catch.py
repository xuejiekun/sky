# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


class BaseRequests:
    default_useragent = r'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
    default_accept_language = r'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'

    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update({'User-Agent': self.default_useragent,
                               'Accept-Language': self.default_accept_language})

    # 设置请求头
    def set_headers(self, useragent):
        self.s.headers.update({'User-Agent': useragent})

    # 设置referer
    def set_referer(self, referer):
        self.s.headers.update({'Referer': referer})

    def clear_referer(self):
        self.s.headers.pop('Referer')

    # get url
    def get_page(self, url, timeout=10, **kwargs):
        try:
            self.r = self.s.get(url, timeout=timeout, **kwargs)
        except:
            return False
        return True

    # 创建bsobj
    def build_bs4(self):
        self.bsobj = BeautifulSoup(self.r.content, 'lxml')

    def text(self, encoding=None):
        if encoding:
            encoding_save = self.r.encoding
            self.r.encoding = encoding
            text = self.r.text
            self.r.encoding = encoding_save
            return text
        return self.r.text

    def json(self, **kwargs):
        return self.r.json(**kwargs)

    # 将请求内容保存为图片
    def save_as_pic(self, filename='1.jpg'):
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
