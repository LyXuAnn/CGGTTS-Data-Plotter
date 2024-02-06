#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :args_plot.py
@Description  :
@Time         :2024/01/10 16:26:06
@Author       :Yaxuan Liu
@Version      :1.0
'''



import argparse
import os

# 创建 ArgumentParser 对象
parser = argparse.ArgumentParser(description='Plot CGGTTS file')

# 添加参数
# parser.add_argument('arg1', help='第一个参数的帮助信息')
# parser.add_argument('--arg2', help='第二个参数的帮助信息') #mytry.py [-h] [--arg2 ARG2] arg1 arg3
# parser.add_argument('arg3', help='help info')
parser.add_argument('arg1_flpath1', help='CGGTTS dir path of sss1')
parser.add_argument('arg2_flpath2', help='CGGTTS dir path of sss2')
parser.add_argument('arg3_outdir', help='directory of the output files')

# 解析参数
args = parser.parse_args()

# 使用参数
print('arg1_flpath1:', args.arg1_flpath1)
print('arg2_flpath2:', args.arg2_flpath2)
print('arg3_outdir:', args.arg3_outdir)


if not os.path.exists(args.arg3_outdir): # 检查文件夹是否存在
    os.makedirs(args.arg3_outdir) # 创建文件夹
