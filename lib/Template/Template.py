# -*- coding: utf-8 -*-
import os

from AbstractVirtualhostTemplate import AbstractVirtualhostTemplate

class TemplateApache(AbstractVirtualhostTemplate):
    __serverName    = ''
    __documentRoot  = ''
    __directoryPath = ''

    # VirtualHostのServerNameを設定
    def setServerName(self,name):
        self.__serverName = name

    def setDocumentRoot(self,name):
        self.__documentRoot = name

    def setDirectoryPath(self,name):
        self.__directoryPath = name

    def setTemplatePath(self,path):
        self._tempalteDir = path

    # 読み込むテンプレート名を変更する
    def setTempalteName(self,name):
        _templateName = name

    # 出力するファイルのデータを作成(ここは作成対象のミドルウェアごとに変わる)
    def create(self):
        filePathName = self._tempalteDir + os.sep + self._templateName
        readData   = self._getReadFileData( filePathName )

        if not self.__directoryPath:
            self.__directoryPath = self.__documentRoot

        data = readData  % ( self.__serverName , self.__documentRoot , self.__directoryPath )
        self._setOutPutData(data)
