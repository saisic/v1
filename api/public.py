#__author__ = 'Administrator'
from dsm.common import DsmCommonApi


class DsmPublicApi(DsmCommonApi):
    '''DSM Public API Object'''

    def _getHostIdByName(self, instanceName):
        hosts = self.hostRetrieveAll()
        for h in hosts:
            if h.name == instanceName:
                return h.ID
        return None

    def getAntiEvent(self, instanceName, timeFlags = None, hostFlags = None, eventFlags = None):
        timeFilter = self.createFactory('TimeFilterTransport')
        hostFilter = self.createFactory('HostFilterTransport')
        eventFilter = self.createFactory('IDFilterTransport')

        hID = None
        if (hostFlags == 'SPECIFIC_HOST') or (hostFlags is None and instanceName):
            hostFilter.type.set("SPECIFIC_HOST")
            hID = self._getHostIdByName(instanceName)
        hostFilter.hostID = hID
        timeFilter.type.set('LAST_24_HOURS')
        eventFilter.id = 0
        eventFilter.operator.set("GREATER_THAN")

        try:
            return self.antiMalwareEventRetrieve(timeFilter, hostFilter, eventFilter)
        except Exception as e:
            print e