""" SunriseSupport Python SDK """
""" Version 1.0 """
""" Author: Integra """
""" Dev: Partha """
""" Licence: None """

import requests, json


class SunriseSupport(object):

    http_origin = ''
    client_id = ''
    client_secret = ''
    access_token = ''
    is_authorized = False

    def __init__(self, *args, **kwargs):
        """ Initiate parameters "access_key, secret_key, http_origin """

        self.http_origin = kwargs['SUPPORT_ORIGIN']
        self.client_id = kwargs['SUPPORT_ACCESS_KEY_ID']
        self.client_secret = kwargs['SUPPORT_SECRET_KEY']
        self.is_authorized, self.access_token = self._getAccessToken()

    def _getAccessToken(self, *args, **kwargs):
        """ This is an internal method to get the access token """
        self.url = self.http_origin + 'support_api/o/token/'
        data = {
            'grant_type' : 'client_credentials',
            'scope':'write'
        }
        resp = requests.post(self.url, data = data, verify=False, auth = (self.client_id, self.client_secret))
        if resp.status_code == 200:
            return (True, resp.json()['access_token'])
        else:
            return (False, "Problem in authenticating your request")


    def _get(self, params = None):
        """ Internal method to get the URL """

        headers = {
            'Authorization' : 'Bearer ' + self.access_token
        }
        resp = requests.get(self.http_origin + self.url, verify=False, headers = headers, params = params)
        
        if resp.status_code == 200:
            return (True, resp.json())
        else:
            return (False, 'Resource not found')


    def _post(self, data = None):
        """ Internal method to post the URL """

        headers = {
            'Authorization' : 'Bearer ' + self.access_token
        }
        resp = requests.post(self.http_origin + self.url, verify=False, headers = headers, data = data)
        
        if resp.status_code == 200:
            return (True, resp)
        else:
            return (False, 'Resource not found')


    def create_ticket(self, product = '',
                            module = '',
                            customer = '', 
                            user = '',
                            support_type = '',
                            sub_type = '',
                            priority = 'MEDIUM',
                            message = '',
                            details = ''):
        """ Create ticket in SunriseSupport """
        
        data = {
            'action':'create_ticket',
            'customer':customer,
            'created_by':user,
            'header': json.dumps({
                'support_type':support_type,
                'sub_type':sub_type,
                'priority':priority,
                'status':'NEW',
                'product':product,
                'module':module
            }),
            'detail': json.dumps({
                'message':message,
                'details':details
            })
        }

        self.url = "support_api/create_ticket/"
        return self._post(data = data)