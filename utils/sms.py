from .melipayamak import Api


def sendSMS(to, text):
    username = '09024809750'
    password = '#DB4Z'
    api = Api(username, password)
    sms = api.sms()
    _from = '50004001809750'
    return sms.send(to, _from, text)
