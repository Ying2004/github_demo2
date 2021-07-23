# -*- coding: utf-8 -*- 
# @Time : 2021/7/23 13:50 
# @Author : ying
# @File : ying_git.py   git分支学习

from faker import Faker

class YingGit:

    def __init__(self):
        # 生成faker对象
        self.faker_obj = Faker(locale='zh_CN')


    def method_1(self):

        # 实现faker生成随机身份证号
        my_card = self.faker_obj.ssn()
        print('我的身份证号是{}'.format(my_card))


if __name__ == '__main__':

    YingGit().method_1()