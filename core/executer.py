
import subprocess
from core.prompt import Prompt

class Executer:
    def __init__(self, exetype:str = None, cmd:str = None, use_input:bool = True):
        self.type = exetype
        self.cmd = cmd
        self.use_input = use_input
        if self.type == 'regen':
            self.llm = Prompt()
    
    def do(self, arg:str = None):
        prp = self.cmd
        if self.use_input and arg is not None:
            prp += arg

        if self.type == 'reply':
            return prp
        if self.type == 'regen':
            rep = self.llm.ask(prp)
            return rep
        if self.type == 'command':
            try:
                cmd = [self.cmd]
                if self.use_input and arg is not None:
                    cmd.append(arg) 
                result = subprocess.run(cmd, stdout = subprocess.PIPE)
                return result.stdout.decode()
            except Exception as e:
                print(e)
                return None

def __test():
    import time
    import os

    exe1 = Executer('reply','hello')
    exe2 = Executer('command','date')
    # exe2 = Executer('command','./test.sh')
    """
    you can execute shell with 'shebang':

    #! /bin/sh
    ...
    ...

    """
    
    print(exe1.do())
    print(exe2.do())

if __name__ == '__main__':
    __test()

