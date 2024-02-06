#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :utility_plot.py
@Description  :
@Time         :2024/01/24 10:23:40
@Author       :Yaxuan Liu
@Version      :1.0
'''

import os

from time_convert import *

class ListDict(object):
    def __init__(self, sat, mjd, refsys):
        self.sat = sat
        self.mjd = mjd
        self.refsys = refsys

class NavListDict(object):
    def __init__(self, nav_system, receiver_name1, receiver_name2, mjd):
        self.nav_system = nav_system
        self.receiver_name1 = receiver_name1
        self.receiver_name2 = receiver_name2
        self.mjd = mjd

def read_file(flname='CGGTTS_BDS_B1_IM01', outdir='/home/liuyaxuan/'):
    """
    @Description :
    
    @Input :
    
    @Returns :
    """
    flname_list = flname.split(os.path.sep) #使用 os.path.sep 来表示平台特定的路径分隔符

    receiverlist = []
    header1 = "SAT CL  MJD  STTIME TRKL ELV AZTH   REFSV      SRSV     REFSYS    SRSYS  DSG IOE MDTR SMDT MDIO SMDI MSIO SMSI ISG FR HC FRC CK"
    header2 = "             hhmmss  s  .1dg .1dg    .1ns     .1ps/s     .1ns    .1ps/s .1ns     .1ns.1ps/s.1ns.1ps/s.1ns.1ps/s.1ns"
    # read file
    with open(flname, "r") as f:
        # header
        while 1:
            line = f.readline().strip("\n")
            if header1 in line:
                break
        if line == "":
            f.close()
        else:
            while 1:
                line = f.readline().strip("\n")
                if line == "":
                    break
                if header2 in line:
                    print("=======start reading data=======")
                    continue
                odom = line.split()
                sat = odom[0] # SAT
                mjd = odom[2] # MJD
                sttime = odom[3] # STTIME
                refsys = odom[9] # REFSYS
                sod = sod_hms(
                    int(sttime[0:2]),
                    int(sttime[2:4]),
                    int(sttime[4:6])
                )
                dmjd = int(mjd) + sod / 86400.0
                receiverlist.append(ListDict(sat, dmjd, float(refsys)))
            f.close()
    # wr.close()
    print("=======sort=======")
    receiverlist.sort(key = lambda x: (x.sat, x.mjd))
    wr = open(os.path.join(outdir, flname_list[-1]+'_tmp'), "w")
    for i in receiverlist:
        # print(i.sat, i.mjd, i.refsys)
        out_line = (
                    i.sat
                    + "   "
                    + str(i.mjd)
                    + "   "
                    + str(i.refsys)
                )
        wr.write(out_line + "\n")
    wr.close
    return receiverlist

def match_cggtts(flpath1, flpath2):
    navlist = []
    seen_pairs = set()

    for file in os.listdir(flpath1):
        if os.path.isfile(os.path.join(flpath1, file)):
            # print(file)
            if file[0] == 'C':
                nav_system = file[0:3]
                receiver_name = file[3:7]
                mjd = file[-6:]
            else:
                nav_system = file[0:2]
                receiver_name = file[2:6]
                mjd = file[-6:]
            pair = (nav_system, mjd)
            
            if pair not in seen_pairs:
                seen_pairs.add(pair)
                for file in os.listdir(flpath2):
                    if os.path.isfile(os.path.join(flpath2, file)):
                        if file[0] == 'C' and file[0:3] == nav_system and file[-6:] == mjd and file[3:7] != receiver_name:
                            # print(file)
                            navlist.append(NavListDict(nav_system, receiver_name, file[3:7], mjd))
                        if file[0] != 'C' and file[0:2] == nav_system and file[-6:] == mjd and file[2:6] != receiver_name:
                            # print(file)
                            navlist.append(NavListDict(nav_system, receiver_name, file[2:6], mjd))
    print('=======finish go through cggtts files of two receivers=======\n')
    return navlist
