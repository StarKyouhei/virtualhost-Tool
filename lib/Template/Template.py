# -*- coding: utf-8 -*-
import os

from AbstractVirtualhostTemplate import AbstractVirtualhostTemplate

class TemplateApache(AbstractVirtualhostTemplate):
    def setTemplatePath(self,path):
        self._tempalteDir = path

    # 読み込むテンプレート名を変更する
    def setTempalteName(self,name):
        _templateName = name
        print _templateName

    def setTempalte(self):
        filePathName = self._tempalteDir + os.sep + self._templateName
        if not os.path.lexists( filePathName ):
            raise Exception( filePathName + "は存在しません")
        # f = open('text.txt')
        # data1 = f.read()  # ファイル終端まで全て読んだデータを返す
        # f.close()
        # print type(data1) # 文字列データ
        print filePathName

    def testmethod(self):
        print "call testmethod"