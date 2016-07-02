# -*- coding: utf-8 -*-

from abc import ABCMeta,abstractmethod

class AbstractVirtualhostTemplate:
    __metaclass__ = ABCMeta

    @abstractmethod
    def setTempalteName(self,name):
        """読み込むテンプレート名を指定"""

    # テンプレート読み込み実装
    @abstractmethod
    def readTempalte(self):
        """セットされたテンプレートを読み込み"""
        return

    def createTemplate(self):
        print self._template
