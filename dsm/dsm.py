#__author__ = 'Administrator'

import suds


class Dsm(object):
    '''The DSM Object'''

    def __init__(self, wsdl, username, password):
        self._wsdl = wsdl
        self._username = username
        self._password = password
        self.client = suds.client.Client(self._wsdl)
        self.service = self.client.service
        self.sID = self._login(username, password)

    def __del__(self):
        self._logout()

    def _login(self, username, password):
        return self.service.authenticate(username, password)

    def _logout(self):
        self.service.endSession(self.sID)
        self.sID = None

    def checksID(self):
        if self.sID is None:
            raise

    def createFactory(self, factoryName):
        return self.client.factory.create(factoryName)