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

    # type
    typeName        = 'apache'
    # OS 特に指定ない場合は空を指定
    osName          = os.sep + 'mac'
    # サーバドメイン名をしてい
    serverName      = 'pythonMake.localhost'
    # ドキュメントルートディレクトリを指定
    documentRoot    = '/var/www/html'
    # 出力ディレクトリ名
    outputDirName   = bootstrap.getSysCurrentDir() + os.sep + 'output'

    # テンプレート作成ようのFactory作成
    TempalteFactory = Factory()
    # テンプレートを読み込むパスを指定
    TempalteFactory.setTemplatePath( bootstrap.getSysCurrentDir() + os.sep +'config/template/' + typeName + osName )
    # とりあえずApacheのテンプレートを作成
    Template = TempalteFactory.create( typeName )
    # ServerNameを設定
    Template.setServerName( serverName )
    # DocumentRootを設定
    Template.setDocumentRoot( documentRoot )
    # テンプレートファイルを作成
    Template.create()
    # 標準出力
    # Template.showData()
    # 外部ファイル出力
    Template.outputData( outputDirName , typeName )