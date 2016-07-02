# -*- coding: utf-8 -*-
import os

from AbstractVirtualhostTemplate import AbstractVirtualhostTemplate

class TemplateApache(AbstractVirtualhostTemplate):
    __serverName    = ''
    __documentRoot  = ''
    __directoryPath = ''
    __outputData    = ''

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
        print _templateName

    # 外部ファイル読み込み
    def __getReadFileData( self, filePathName ):
        if not os.path.lexists( filePathName ):
            raise Exception( filePathName + "は存在しません")

        file = open( filePathName )
        data = file.read()
        file.close()
        return data

    def create(self):
        filePathName = self._tempalteDir + os.sep + self._templateName
        readData   = self.__getReadFileData( filePathName )

        if not self.__directoryPath:
            self.__directoryPath = self.__documentRoot

        self.__outputData = readData  % ( self.__serverName , self.__documentRoot , self.__directoryPath )

    def showData(self):
        print self.__outputData