# -*- coding: utf-8 -*-

from abc import ABCMeta,abstractmethod

class AbstractFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self,name):
        """クラスを作成"""
