#__author__ = 'Administrator'

from dsm.dsm import Dsm


class DsmVmApi(Dsm):
    ''' Virtual Machines Management APIs Object '''

    def virtualCreate(self, virtual):
        self.checksID()
        return self.service.virtualCreate(virtual, self.sID)

    def virtualDelete(self, id):
        self.checksID()
        return self.service.virtualDelete(id, self.sID)

    def virtualRetrieve(self, id):
        self.checksID()
        return self.service.virtualRetrieve(id, self.sID)

    def virtualRetrieveAll(self, id):
        self.checksID()
        return self.service.virtualRetrieveAll(self.sID)

    def virtualSynchronize(self, virtualID):
        self.checksID()
        return self.service.virtualSynchronize(virtualID, self.sID)

    def virtualUpdate(self, virtual):
        self.checksID()
        return self.service.virtualUpdate(virtual, self.sID)
