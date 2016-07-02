# -*- coding: utf-8 -*-

import sys,os

def getSysCurrentDir():
    currentDirName = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return currentDirName

# 読み込むディレクトリを追加
def setSysPathAppend( name ):
    # カレントディレクトリパスを取得
    curDir      = getSysCurrentDir()
    checkDir    = curDir + '/' +name
    if not os.path.lexists( checkDir ):
        raise Exception( checkDir + "は存在しません")
    sys.path.append('/ufs/guido/lib/python')
