#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :main.py
@Description  :plot CGGTTS format file
@Time         :2023/12/20 10:25:46
@Author       :Yaxuan Liu
@Version      :1.0
'''


import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

from args_plot import *
from plot_flparse import *


if __name__ == "__main__":
    navlist = match_cggtts(args.arg1_flpath1, args.arg2_flpath2)
    for cggtts_file in navlist:
        print('=======nav system: %s, %s, %s and %s======='
                %(cggtts_file.nav_system, cggtts_file.mjd, 
                cggtts_file.receiver_name1, cggtts_file.receiver_name2))
        flname1 = cggtts_file.nav_system + cggtts_file.receiver_name1 + cggtts_file.mjd
        flname2 = cggtts_file.nav_system + cggtts_file.receiver_name2 + cggtts_file.mjd
        receiver01 = read_file(os.path.join(args.arg1_flpath1, flname1), args.arg3_outdir)
        receiver02 = read_file(os.path.join(args.arg2_flpath2, flname2), args.arg3_outdir)

        print("=======difference=======")
        outfile_prefix = cggtts_file.nav_system + cggtts_file.receiver_name1 + cggtts_file.receiver_name2 + cggtts_file.mjd
        diff = [(i.sat, i. mjd, (i.refsys - j.refsys)/10) for i in receiver01 for j in receiver02 if i.sat == j.sat and i.mjd == j.mjd]
        wr = open(os.path.join(args.arg3_outdir, outfile_prefix + '_diff'), "w") # TODO outdir
        for i in diff:
            # print(i[0], i[1], i[2])
            out_line = (
                        i[0]
                        + "   "
                        + str(i[1])
                        + "   "
                        + str(i[2])
                    )
            wr.write(out_line + '\n')
        wr.close

        print("=======summary by mjd=======")
        if len(diff) == 0:
            print('empty match')
        else: 
            col_refsys = [row[2] for row in diff]
            col_mjd= [row[1] for row in diff]
            
            sum_bymjd = []
            for mjd in list(set(col_mjd)):
                diff_bymjd = [row[2] for row in diff if row[1] == mjd]
                pts_bymjd = len(diff_bymjd)
                if pts_bymjd != 0:
                    ave_bymjd = sum(diff_bymjd) / pts_bymjd
                    median_bymjd = np.median(diff_bymjd)
                    rms_bymjd = np.sqrt(np.mean(np.square(diff_bymjd)))
                    std_bymjd = np.std(diff_bymjd)
                    sum_bymjd.append((mjd, pts_bymjd, ave_bymjd, std_bymjd, median_bymjd, rms_bymjd))
            sum_bymjd.sort(key = lambda x: x[0])
            wr = open(os.path.join(args.arg3_outdir, outfile_prefix + '_summary_bymjd'), "w")
            out_line = (
                        "mjd"
                        + "   "
                        + "pts"
                        + "   "
                        + "ave"
                        + "   "
                        + "std"
                        + "   "
                        + "median"
                        + "   "
                        + "rms"
                    )
            wr.write(out_line + "\n")
            for i in sum_bymjd:
                out_line = (
                            str(i[0])
                            + "   "
                            + str(i[1])
                            + "   "
                            + str(i[2])
                            + "   "
                            + str(i[3])
                            + "   "
                            + str(i[4])
                            + "   "
                            + str(i[5])
                        )
                wr.write(out_line + '\n')
            wr.close

            print("=======summary=======")
            pts = len(diff)
            ave = sum(col_refsys)
            ave = ave / pts
            median = np.median(col_refsys)
            # 均方根值，也称方均根值或有效值，它的计算方法是先平方、再平均、然后开方
            rms = np.sqrt(np.mean(np.square(col_refsys)))
            std = np.std(col_refsys)
            wr = open(os.path.join(args.arg3_outdir, outfile_prefix + '_summary'), "w") # TODO outdir
            out_line = (
                        "pts"
                        + "   "
                        + "ave"
                        + "   "
                        + "std"
                        + "   "
                        + "median"
                        + "   "
                        + "rms"
                    )
            wr.write(out_line + "\n")
            out_line = (
                        str(pts)
                        + "   "
                        + str(ave)
                        + "   "
                        + str(std)
                        + "   "
                        + str(median)
                        + "   "
                        + str(rms)
                    )
            wr.write(out_line + "\n")
            wr.close
            
            print("=======plot=======")
            plt.figure(figsize=(10, 4))  # 设置图的长宽比

            color_map = {'G02': 'black', 'G03': 'red', 'G04': 'blue', 'G05': 'green',
                        'G06': 'yellow', 'G07': 'purple', 'G08': 'orange', 'G09': 'cyan',
                        'G10': 'magenta', 'G11': '#FF5733', 'G12': 'darkgreen', 'G13': 'lightblue',
                        'G14': 'pink', 'G15': 'brown', 'G16': '#808080', 'G17': '#660066',
                        'G18': 'navy', 'G19': 'indigo', 'G20': 'maroon', 'G21': 'silver',
                        'G22': 'lime', 'G23': 'aqua', 'G24': 'fuchsia', 'G25': 'skyblue',
                        'G26': 'tan', 'G27': 'salmon', 'G28': 'orchid', 'G29': 'slategray',
                        'G30': 'peru', 'G31': 'khaki', 'G32': 'steelblue',

                        'C19': 'black', 'C20': 'red', 'C21': 'blue', 'C22': 'green',
                        'C23': 'yellow', 'C24': 'purple', 'C25': 'orange', 'C26': 'cyan',
                        'C27': 'magenta', 'C28': '#FF5733', 'C29': 'darkgreen', 'C30': 'lightblue',
                        'C32': 'pink', 'C33': 'brown', 'C34': '#808080', 'C35': '#660066',
                        'C36': 'navy', 'C37': 'indigo', 'C38': 'maroon', 'C39': 'silver',
                        'C40': 'lime', 'C41': 'aqua', 'C42': 'fuchsia', 'C43': 'skyblue',
                        'C44': 'tan', 'C45': 'salmon', 'C46': 'orchid', 'C01': 'slategray',
                        'C02': 'peru', 'C03': 'khaki', 'C08': 'steelblue', 'C10': '#006400',
                        'C13': '#800000', 'C60': '#4B0082', 'C16': '#FFD700', 'C06': 'plum',
                        'C12': 'crimson', 'C09': 'teal', 'C04': 'olive', 'C07': 'violet',
                        'C11': '#8A2BE2', 'C14': '#FF1493', 'C59': '#00FF7F','C05': '#1E90FF',

                        'E03': 'black', 'E05': 'red', 'E09': 'blue', 'E15': 'green',
                        'E24': 'yellow', 'E25': 'purple', 'E31': 'orange', 'E34': 'cyan',
                        'E13': 'magenta', 'E08': '#FF5733', 'E02': 'darkgreen', 'E04': 'lightblue',
                        'E07': 'pink', 'E10': 'brown', 'E11': '#808080', 'E12': '#660066',
                        'E19': 'navy', 'E21': 'indigo', 'E26': 'maroon', 'E27': 'silver',
                        'E30': 'lime', 'E33': 'aqua', 'E36': 'fuchsia'}  # TODO 缺少 glonass--R
            colors = [color_map[row[0]] for row in diff]  # 根据首列的值获取对应颜色
            # extra_colors_2 = [ '#FFA500']
            plt.scatter(col_mjd, col_refsys, color=colors, s=10) # plt.scatter(x, y, color='black', s=10)  设置点的颜色为黑色，点的大小为100
            plt.xlabel("mjd")
            plt.ylabel("difference between two receivers (ns)")
            # plt.ylim(-12, -2)
            plt.ylim(np.min(col_refsys) - 2, np.max(col_refsys) + 2)
            plt.text(0.98, 0.98, "ave: %.2f, std: %.2f, median: %.2f, rms: %.2f" %(ave, std, median, rms), ha='right', va='top', transform=plt.gca().transAxes, fontsize=10)
            # plt.show()
            # 设置 x 轴格式
            plt.ticklabel_format(style='plain', axis='x')  # 禁用 x 轴上的科学计数法
            plt.gca().xaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))  # 设置 x 轴保留一位小数
            plt.savefig(os.path.join(args.arg3_outdir, outfile_prefix + "_fig.png"), pad_inches=None, bbox_inches="tight", dpi=300)  # TODO outdir
            plt.close() # 关闭之前的图形窗口，释放内存
            # print('=======done=======\n')

            fig, axes = plt.subplots(nrows = 5, ncols = 1, figsize=(8,12)) # 创建一个包含5行1列的子图布局
            title_map = {1: 'pts', 2:'ave', 3:'std', 4:'median', 5:'rms'}
            for i, ax in enumerate(axes):
                ax.plot([row[0] for row in sum_bymjd], [row[i+1] for row in sum_bymjd])
                ax.set_xlabel("mjd")
                ax.set_title(title_map[i+1], fontsize=12, fontweight='bold')
                ax.ticklabel_format(style='plain', axis='x')  # 禁用 x 轴上的科学计数法
                ax.xaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))  # 设置 x 轴保留一位小数

            plt.tight_layout()
            plt.savefig(os.path.join(args.arg3_outdir, outfile_prefix + "_fig_summary.png"), pad_inches=None, bbox_inches="tight", dpi=300)  # TODO outdir
            plt.close() # 关闭之前的图形窗口，释放内存
        print('=======done=======\n')