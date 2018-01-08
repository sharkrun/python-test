#! /usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ziv·chan'

from lxml import etree
from PIL import Image
import requests
import re
from lxml import html


user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
referer = 'https://192.168.18.250/login'

user_passwd = {"username": "YWRtaW4=", "password": "MTIz"}

headers = {
    'User-Agent': user_agent,
    'Connection': 'keep-alive',
    'Host': '192.168.18.250',
    'Origin': 'https://192.168.18.250',
    'Referer': referer
}

session = requests.session()

# 注意URL的选择
url = 'https://192.168.18.250/login'
with session as s:
    result = s.get(url, verify=False)
# pageCode = s.text
tree = html.fromstring(result.text)
print tree.tag
print tree.xpath("password")
authenticity_token = list(set(tree.xpath("//input[@id='_username']/@value")))[0]
print authenticity_token
# authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
pattern = re.compile('password" name="(.*?)".*?name="vk" value="(.*?)".*?"capId" value="(.*?)"', re.S)
print 'pattern:', pattern
pageCode = ''
items = re.findall(pattern, pageCode)[0]
password, vk, capId = items


cap_url = 'http://weibo.cn/interface/f/ttt/captcha/show.php?cpt=' + items[2]
captcha = session.get(cap_url, headers=headers)
with open('cap.png', 'wb') as f:
    f.write(captcha.content)
    f.close()
    im = Image.open('cap.png')
    im.show()
    im.close
    cap_code = raw_input('请输入验证码:')

form_data = {
    'mobile': '18362972928',
    password: 'ChelseaFC.1',
    'code': cap_code,
    'remember': 'on',
    'backURL': 'http%3A%2F%2Fweibo.cn%2F',
    'backTitle': '微博',
    'tryCount': '',
    'vk': vk,
    'capId': capId,
    'submit': '登录'
}

session.post(url, data=form_data, headers=headers)

url_logined = 'http://weibo.cn/'
html_2 = session.get(url_logined)
html_2.encoding = 'utf-8'
pageCode_2 = html_2.content
Selector = etree.HTML(pageCode_2)
content = Selector.xpath('//span[@class="ctt"]')
for each in content:
    text = each.xpath('string(.)')
    print text
