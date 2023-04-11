from llmapi_cli.llmclient import LLMClient
import json
import os

class Prompt:
    def __init__(self, apikey:str = None):
        if apikey is None:
            key = os.environ.get('LLMAPI_IO_KEY')
        else:
            key = apikey

        self.client = LLMClient(bot_type='chatgpt',apikey=key)
        self.client.start_session()

    def ask(self, prompt:str):
        ret,rep = self.client.ask(prompt=prompt)
        return rep if ret == 0 else None
