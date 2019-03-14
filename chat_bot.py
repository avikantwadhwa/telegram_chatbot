import json
import requests

class telegram_chatbot():
    def __init__(self,config):
        self.token=self.read_token_from_config_file(config)
        self.base="https://api.telegram.org/bot{}/".format(self.token)
        
        