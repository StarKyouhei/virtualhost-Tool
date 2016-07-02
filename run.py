#!/usr/bin/python
# -*- coding: utf-8 -*-

from config import bootstrap
if __name__ == "__main__":
    # 読み込むディレクトリを登録 ライブラリー
    bootstrap.setSysPathAppend('lib/Template')

    import TemplateApache
    tet = TemplateApache.TemplateApache()
    tet.setTempalteName('default')