from elastalert.alerts import Alerter, BasicMatchString
from support_api import SunriseSupport #Import from your location
import sys
class Worker_supporthub(Alerter):

    # By setting required_options to a set of strings
    # You can ensure that the rule config file specifies all
    # of the options. Otherwise, ElastAlert will throw an exception
    # when trying to load the rule.
    required_options = set(['SUPPORT_ORIGIN'])

    # Alert is called
    def alert(self, matches):

        # Matches is a list of match dictionaries.
        # It contains more than one match when the alert has
        # the aggregation option set

        for match in matches:
            message=match['@message']
            index_name=match['_index']
            message=str(index_name)+'\n'+message
            kibana_url=self.rule['kibana_doc_url']+self.rule['index']+'/'+index_name+'/logs/?id='+match['_id']
            if match['@fields'].has_key('stack_trace'):
                details=match['@fields']['stack_trace']
                details=details+'\n'+'kibana_url: '+kibana_url
                

                

            else:
                details='kibana_url: '+kibana_url
            connector = {
                'SUPPORT_ORIGIN':self.rule['SUPPORT_ORIGIN'],
                'SUPPORT_ACCESS_KEY_ID':self.rule['SUPPORT_ACCESS_KEY_ID'],
                'SUPPORT_SECRET_KEY':self.rule['SUPPORT_SECRET_KEY']
            }
            SpObj = SunriseSupport(**connector)
            data = {
                'product': 'SunriseRecon',
                'module':'Setup',
                'customer':'SUPPORTADMIN', #Dynamic
                'user':'QARECON',
                'support_type':'RECON_LOGGER',
                'sub_type':'BUGS',
                'priority':'MEDIUM',
                'message':str(message)[:98],
                'details':details
            }
            try:
                data.update({'message':str(sys.argv[2]+"\\n"+sys.argv[3])[:98], 'details':sys.argv[1]})
            except:
                pass
            print SpObj.create_ticket(**data)


              

    # get_info is called after an alert is sent to get data that is written back
    # to Elasticsearch in the field "alert_info"
    # It should return a dict of information relevant to what the alert does
    def get_info(self):
        return {'type': 'Worker_supporthub Alerter',
                'supporthub_url': self.rule['SUPPORT_ORIGIN']}

class Webserver_supporthub(Alerter):

    # By setting required_options to a set of strings
    # You can ensure that the rule config file specifies all
    # of the options. Otherwise, ElastAlert will throw an exception
    # when trying to load the rule.
    required_options = set(['SUPPORT_ORIGIN'])

    # Alert is called
    def alert(self, matches):

        # Matches is a list of match dictionaries.
        # It contains more than one match when the alert has
        # the aggregation option set

        for match in matches:
            message=match['message']
            index_name=match['_index']
            message=str(index_name)+'\n'+message
            kibana_url=self.rule['kibana_doc_url']+self.rule['index']+'/'+index_name+'/logs/?id='+match['_id']
            if match.has_key('stack_trace'):
                details=match['stack_trace']
                details=details+'\n'+'kibana_url: '+kibana_url
                

                

            else:
                details='kibana_url: '+kibana_url
            connector = {
                'SUPPORT_ORIGIN':self.rule['SUPPORT_ORIGIN'],
                'SUPPORT_ACCESS_KEY_ID':self.rule['SUPPORT_ACCESS_KEY_ID'],
                'SUPPORT_SECRET_KEY':self.rule['SUPPORT_SECRET_KEY']
            }
            SpObj = SunriseSupport(**connector)
            data = {
                'product': 'SunriseRecon',
                'module':'Setup',
                'customer':'SUPPORTADMIN', #Dynamic
                'user':'QARECON',
                'support_type':'RECON_LOGGER',
                'sub_type':'BUGS',
                'priority':'MEDIUM',
                'message':str(message)[:98],
                'details':details
            }
            try:
                data.update({'message':str(sys.argv[2]+"\\n"+sys.argv[3])[:98], 'details':sys.argv[1]})
            except:
                pass
            print SpObj.create_ticket(**data)


              

    # get_info is called after an alert is sent to get data that is written back
    # to Elasticsearch in the field "alert_info"
    # It should return a dict of information relevant to what the alert does
    def get_info(self):
        return {'type': 'Worker_supporthub Alerter',
                'supporthub_url': self.rule['SUPPORT_ORIGIN']}