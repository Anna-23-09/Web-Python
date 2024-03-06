from zeep import Client
import pytest

wsdl = "http://dss.cryptopro.ru/verify/service.svc?wsdl"
sign = ""

client = Client(wsdl=wsdl)


# print(client.service.VerifySignature("CMS", sign)['Result'])

def test_step_1():
    assert client.service.VerifySignature("CMS", sign)['Result']
