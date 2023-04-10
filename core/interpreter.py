
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
        exetype = link['action']['type']
        cmds = link['action']['contents']
        workers = []
        for cmd in cmds:
            executer = Executer(exetype,cmd)
            workers.append(executer)

        return index,workers
         
