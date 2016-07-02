# -*- coding: utf-8 -*-

from abc import ABCMeta,abstractmethod

class AbstractVirtualhostTemplate:
    __metaclass__ = ABCMeta

    # デフォルトで読み込むファイル名を設定
    _templateName = 'default.conf'
    # 読み込むテンプレートのディレクトリ名
    _tempalteDir  = '';

    @abstractmethod
    def setTemplatePath(self,path):
        """読み込むテンプレートのディレクトリを設定"""

    @abstractmethod
    def setTempalteName(self,name):
        """読み込むテンプレート名を指定"""

    # テンプレート読み込み実装
    @abstractmethod
    def setTempalte(self):
        """セットされたテンプレートを読み込み"""
        return

    def createTemplate(self):
        print self._template
