#-*-coding:UTF-8-*-
#__author__ = 'Administrator'

from api.public import DsmPublicApi
from common import log as logging
from common.gettextutils import _

import service

if __name__ == '__main__':

    wsdl = 'https://192.168.0.168:4119/webservice/Manager?WSDL'
    username = 'admin'
    password = '1234!@#$'
    LOG = logging.getLogger('nova.all')

    api = DsmPublicApi(wsdl, username, password)

    print api.getApiVersion()
    print api.getManagerTime()

    launcher = service.process_launcher()

    for binary in ['mod1', 'mod2', 'mod3']:
        topic = None
        manager = None

        try:
            launcher.launch_service(service.Service.create(binary=binary,
                                                           topic=topic,
                                                           manager=manager))
        except (Exception, SystemExit):
            LOG.exception(_('Failed to load %s'), binary)
    launcher.wait()
