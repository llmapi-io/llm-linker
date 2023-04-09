

class Executer:
    def __init__(self, exetype:str = None, cmd:str = None):
        self.type = exetype
        self.cmd = cmd
    
    def do(self, arg:str = None):
        if self.type == 'reply':
            print(f'doing {self.cmd}')
            return self.cmd
        if self.type == 'command':
            print(f'doing {self.cmd}')
            return self.cmd
