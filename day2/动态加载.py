#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Beam
@Mail:506556658@qq.com
@file: 动态加载.py
@time: 2017/4/15 9:59
"""

import importlib
aa = importlib.import_module('lib.aa')
print(aa.P().name)
