import json
import requests
import configparser as cfg

class telegram_chatbot():
    def __init__(self,config):
        self.token=self.read_token_from_config_file(config)
        self.base="https://api.telegram.org/bot{}/".format(self.token)
        
        def get_updates(self,offset=None):
            url=self.base + "/getUpdates?&timeout=100"
            if offset:
                url=url+"&offset={}".format(offset+1)
                r=requests.get(url)
                return json.loads(r.content)
        
        def sendMessage(self,msg,chat_id):
            url=self.base + "/sendMessage?chat_id={}&text={}".foramt(chat_id,msg)
            if msg is not None:
                r=requests.get(url)

        def read_token_from_config_file(config):
            parser=cfg.ConfigParser()
            parser.read(config)
            return parser.get('creds','token')