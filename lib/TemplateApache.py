# -*- coding: utf-8 -*-

from AbstractVirtualhostTemplate import AbstractVirtualhostTemplate

class TemplateApache(AbstractVirtualhostTemplate):
    __templateName = ''

    def setTempalteName(self,name):
        __templateName = name
        print __templateName

    def readTempalte(self):
        print self._templatePath

    def testmethod(self):
        print "call testmethod"