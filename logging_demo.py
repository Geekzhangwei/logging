#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import logging
import time

retval = os.getcwd()  # 获取当前目录


# 获取当前时间，并按照标准化格式输出
fileDay = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 判断是否存在日志文件夹
if not os.path.exists(retval+'/logs'):
    os.mkdir(retval+'/logs')

# 创建、读取文件，注意.log与.txt差别不大
file = open(retval + '/logs/' + fileDay + '.log', 'w')

# 写入文件
file.write('hello')

# 关闭文件
file.close()

