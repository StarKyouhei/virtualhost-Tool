# -*- coding: utf-8 -*-

from abc import ABCMeta,abstractmethod

class AbstractFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def setTemplatePath(self,path):
        """読み込むテンプレートのディレクトリを設定"""

    @abstractmethod
    def create(self,name):
        """クラスを作成"""
