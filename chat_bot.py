import json
import requests
import configparser as cfg

class telegram_chatbot:

    def read_token_from_config_file(self,config):
            parser=cfg.ConfigParser()
            parser.read(config)
            return parser.get('creds','token')

    def __init__(self,config):
        self.token="token"
        self.base="https://api.telegram.org/bot{}".format(self.token)
        
    def get_updates(self,offset=None):
            url=self.base + "/getUpdates?&timeout=100"
            if offset:
                url=url+"&offset={}".format(offset+1)
            r=requests.get(url)
            return r.json()
        
    def sendMessage(self,msg,chat_id):
            url=self.base + "/sendMessage?chat_id={}&text={}".format(chat_id,msg)
            if msg is not None:
                r=requests.get(url)

     
