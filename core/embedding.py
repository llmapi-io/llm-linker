from llmapi_cli.llmclient import LLMClient
import json
import os

class Embedding:
    def __init__(self, apikey:str = None):
        if apikey is None:
            key = os.environ.get('LLMAPI_IO_KEY')
        else:
            key = apikey

        self.client = LLMClient(bot_type='gpt-embedding',apikey=key)
        self.client.start_session()

    def embedding(self, prompt:str):
        ret,rep = self.client.ask(prompt=prompt)
        if ret != 0:
            print(ret,rep)
            return None
        return rep
