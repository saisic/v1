#-*-coding:UTF-8-*-
#__author__ = 'Administrator'

from api.public import DsmPublicApi
from rest.restfull import Restful


class TestChen(object):
    def __init__(self):
        self.rest = Restful()

    def test(self):
        attrB = self.rest.getAttribute('b')
        return '{\"vpc\":'+attrB+'}'

    def testGET(self):
        a = self.rest.getAttribute('a')
        v = self.rest.query('u')
        if not v:
            v = ''
        elif v is True:
            v = '\"true\"'
        return '{\"test\":'+a+',\"value\":'+v+'}'

    def testPost(self):
        p = self.rest.query('p')
        v = self.rest.query('v')
        return '{\"q\":'+p+',\"v\":'+v+'}'


if __name__ == '__main__':

    wsdl = 'https://192.168.0.168:4119/webservice/Manager?WSDL'
    username = 'admin'
    password = '1234!@#$'

    api = DsmPublicApi(wsdl, username, password)

    print api.getApiVersion()
    print api.getManagerTime()

    mytest = TestChen()

    mytest.rest.run()
    mytest.rest.router('/wm/[a]?')(mytest.testGET())