
from core.embedding import Embedding
from core.executer import Executer

class Interpreter:
    def __init__(self):
        self.embed = Embedding()

    def decode(self, link:dict):
        """
        return embedding as index
        return executer objects as worker
        """
        index = self.embed.embedding(link['task'])
        if index is None:
            return None,None
        
        workers = []
        for act in link['actions']:
            exetype = act['type']
            cmd = act['content']
            use_input = True if act['input'] != '_NONE_' else False
            executer = Executer(exetype,cmd, use_input)
            workers.append(executer)

        return index,workers
         
