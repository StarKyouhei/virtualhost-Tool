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
    typeName = raw_input( "どのアプリケーションのconfを作成しますか？ (default:apache) : " )
    if not typeName :
        typeName        = 'apache'

    print "Select Type :" + typeName + "\n"

    # OS 特に指定ない場合は空を指定
    osName = raw_input( "どのOSのテンプレートを利用しますか？ (default:mac) : " )
    if not osName :
        osName          = os.sep + 'mac'

    print "OS Type :" + osName + "\n"

    # OS 特に指定ない場合は空を指定
    serverName = raw_input( "VirtualHostのServerNameは？ (default:pythonMake.localhost) : " )
    if not serverName :
        # サーバドメイン名をしてい
        serverName      = 'pythonMake.localhost'

    print "VirtualHost ServerName :" + serverName + "\n"

    # ドキュメントルートディレクトリを指定
    documentRoot = raw_input( "VirtualHostのドキュメントルートディレクトリは？ (default:/var/www/html) : " )
    if not documentRoot :
        documentRoot    = '/var/www/html'

    print "VirtualHost DocumentRoot :" + documentRoot + "\n"


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

    result = raw_input( "ファイルの出力を行いますか? y/n : " )
    print "Select Resutl :" + result + "\n"

    if result == "y" :
        # 出力ファイル名
        outFileName = raw_input( "出力するファイル名は？ (default:" + typeName + ") : " )
        if not outFileName :
            outFileName = typeName

        print "Output file name :" + outFileName + "\n"

        # 出力ディレクトリ名
        outputDirName   = bootstrap.getSysCurrentDir() + os.sep + 'output'
        # 外部ファイル出力
        Template.outputData( outputDirName , outFileName )
    else :
        # 標準出力
        Template.showData()

    print "Bye 🐷" + "\n"
