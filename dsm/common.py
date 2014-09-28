#__author__ = 'Administrator'

from dsm import Dsm


class DsmCommonApi(Dsm):
    '''The Dsm Common APIs Object'''

    def getApiVersion(self):
        return self.service.getApiVersion()

    def getManagerTime(self):
        return self.service.getManagerTime()