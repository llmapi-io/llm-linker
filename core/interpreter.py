
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
        exetype = link['action']['type']
        cmds = link['action']['commands']
        workers = []
        for cmd in cmds:
            executer = Executer(exetype,cmd)
            workers.append(executer)

        return index,workers
         
