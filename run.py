#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from config import bootstrap
if __name__ == "__main__":
    # 読み込むディレクトリを登録 ファクトリー系
    libName = 'lib'
    bootstrap.setSysPathAppend( libName + os.sep + 'Factory')
    # テンプレート系
    bootstrap.setSysPathAppend( libName + os.sep + 'Template')

    from TemplateFactory import Factory

    typeName = 'apache'
    # テンプレート作成ようのFactory作成
    TempalteFactory = Factory()
    # テンプレートを読み込むパスを指定
    TempalteFactory.setTemplatePath( bootstrap.getSysCurrentDir() + os.sep +'config/template/' + typeName)
    # とりあえずApacheのテンプレートを作成
    Tempalte = TempalteFactory.create( typeName )
    Tempalte.setTempalte()