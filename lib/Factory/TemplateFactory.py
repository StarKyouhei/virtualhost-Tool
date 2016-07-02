# -*- coding: utf-8 -*-

from AbstractFactory import AbstractFactory

import Template

class Factory(AbstractFactory):
    # 生成するクラス
    __TempalteClass = None;
    # 読み込むテンプレートのディレクトリ名
    __tempalteDir  = '';

    def setTemplatePath(self,path):
        self.__tempalteDir = path

    def create(self,name):
        if name == 'apache' :
            self.__TempalteClass = Template.TemplateApache()
        else :
            raise Exception("Factoryに登録されていません")

        #読み込むテンプレートのディレクトリ名を指定
        self.__TempalteClass.setTemplatePath( self.__tempalteDir )

        return self.__TempalteClass