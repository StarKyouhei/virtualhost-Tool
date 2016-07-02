# -*- coding: utf-8 -*-

from AbstractFactory import AbstractFactory

import Template

class Factory(AbstractFactory):
    __TempalteClass = None;

    def create(self,name):
        if name == 'apache' :
            self.__TempalteClass = Template.TemplateApache()
        else :
            raise Exception("Factoryに登録されていません")

        return self.__TempalteClass