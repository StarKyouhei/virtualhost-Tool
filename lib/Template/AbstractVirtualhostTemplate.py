# -*- coding: utf-8 -*-
import os
import datetime

from abc import ABCMeta,abstractmethod

class AbstractVirtualhostTemplate:
    __metaclass__ = ABCMeta

    # デフォルトで読み込むファイル名を設定
    _templateName = 'default.conf'
    # 読み込むテンプレートのディレクトリ名
    _tempalteDir    = '';
    # 生成される出力データ
    _outputData     = ''
    # 出力の際の拡張子
    __Extension     = '.conf'

    @abstractmethod
    def setTemplatePath(self,path):
        """読み込むテンプレートのディレクトリを設定"""

    @abstractmethod
    def setTempalteName(self,name):
        """読み込むテンプレート名を指定"""

    # テンプレート読み込み実装
    @abstractmethod
    def create(self):
        """セットされたテンプレートを作成"""
        return

    # 出力データの設定
    @classmethod
    def _setOutPutData(self,data):
        self._outputData = data

    # 出力データの取得
    @classmethod
    def _getOutPutData(self):
        return self._outputData

    # 外部ファイル読み込み
    @classmethod
    def _getReadFileData( self, filePathName ):
        if not os.path.lexists( filePathName ):
            raise Exception( filePathName + "は存在しません")

        file = open( filePathName )
        data = file.read()
        file.close()
        return data

    # 外部ファイル書き込み
    @classmethod
    def _dataWriteFile( self , filePathName ):
        f = open( filePathName , 'w') # 書き込みモードで開く
        data = self._getOutPutData()
        f.writelines( data ) # シーケンスが引数。
        f.close()

    def __getFileSuffix(self):
        date = datetime.datetime.today()
        suffix = date.strftime("%Y-%m-%d")
        return '_' + suffix + self.__Extension

    # 作成ファイルの標準出力
    def showData(self):
        print self._getOutPutData()

    def outputData(self,path,name ):
        filePahtName = path + os.sep + name + self.__getFileSuffix()
        self._dataWriteFile( filePahtName )
        print 'make file' + filePahtName