#!/usr/bin/python
# -*- coding: utf-8 -*-

from config import bootstrap
if __name__ == "__main__":
    # 読み込むディレクトリを登録 ファクトリー系
    bootstrap.setSysPathAppend('lib/Factory')
    # テンプレート系
    bootstrap.setSysPathAppend('lib/Template')

    from TemplateFactory import Factory

    FactoryMethod = Factory()
    FactoryMethod.create('apache')