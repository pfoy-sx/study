#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/14 14:46
# @Author  : Beam
# @Site    :
# @File    : Calculator.py
# @Software: PyCharm

# 8*((9+7/2)-1))
# 提示：re.search(r'\([^()]+\)',s).group()

import re


#乘除运算
def mul_div(bra):
    cal = re.search(r'[\d\.]+[\*\/]{1}[\+\-]?[\d\.]+',bra)
    if not cal:
        return bra
    jud = re.search(r'[\d\.]+[\*\/]{1}[\+\-]?[\d\.]+', bra).group()  # 获取匹配的内容
    if len(jud.split('*')) > 1:
        n1, n2 = jud.split('*')
        value = float(n1) * float(n2)
    else:
        n1, n2 = jud.split('/')
        if float(n2) == 0:
            print('输入的格式错误,程序退出')
            exit()
        value = float(n1) / float(n2)
    one, two = re.split(r'[\d\.]+[\*\/]{1}[\+\-]?[\d\.]+', bra, 1)
    new_formula = '%s%s%s' % (one, value, two)
    return mul_div(new_formula)  # 递归处理,直到没有乘除,然后返回字符串bra


#加减运算
def add_sub(bra):
    #考虑括号出来的内容是负数
    bra = bra.replace('--', '+')
    bra = bra.replace('++', '+')
    bra = bra.replace('-+', '-')
    bra = bra.replace('+-', '-')
    jud = re.search(r'[\d\.]+[\+\-]{1}[\d\.]+', bra)
    if not jud:
        return bra
    content = re.search(r'[\-]?[\d\.]+[\+\-]{1}[\d\.]+', bra).group()
    if len(content.split('+')) > 1:
        n1, n2 = content.split('+')
        value = float(n1) + float(n2)
    elif content.startswith('-'):  # 考虑 -3-3 这种负号开头的情况
        n1, n2, n3 = content.split('-')
        value = -float(n2) - float(n3)
    else:
        n1, n2 = content.split('-')
        value = float(n1) - float(n2)
    # 接下来就要重组字符串,然后返回
    before, after = re.split(r'[\-]?[\d\.]+[\+\-]{1}[\d\.]+', bra, 1)
    new_formula = "%s%s%s" % (before, value, after)
    return add_sub(new_formula)


def calculation(formula):
    jud = re.search(r'\(([^()]+?)\)', formula)
    #如果没有匹配到括号，则直接先乘除后加减返回结果
    if not jud:
        rest1 = mul_div(formula)
        rest2 = add_sub(rest1)
        return rest2
    else:
        bra = re.search(r'\(([^()]+?)\)', formula).group(1)     #group(0) 表示带括号 group(1)不带括号
        rest1 = mul_div(bra)
        rest2 = add_sub(rest1)
    one,temp,two = re.split(r'\(([^()]+?)\)', formula,1)
    new_formula = '%s%s%s' %(one,rest2,two)
    return calculation(new_formula)


def main():
    while True:
        formula = input('请输入一条算式(q for exit):').strip()
        if formula.lower() == 'q':
            print('退出程序！')
            exit()
        if re.search(r'[^0-9\+\-\*\/\(\)\.]',formula):
            print('输入有误，请重新输入')
            continue
        else:
            result = calculation(formula)
            print('Result：'+ result)
            #print(eval(formula))

if __name__ == '__main__':
    main()