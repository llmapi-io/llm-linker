from core.interpreter import Interpreter
import numpy as np
import os

def distance(embedding1: dict, embedding2: dict) -> float:
    a = embedding1
    b = embedding2
    dot_product = np.dot(a, b)
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    cosine_sim = dot_product / (a_norm * b_norm)
    return cosine_sim

class Linker:
    def __init__(self, apikey:str = None):
        if apikey is not None:
            os.environ['LLMAPI_IO_KEY'] = apikey
        self.inter = Interpreter()
        self.links = []

    def add(self, link:dict):
        """
        link:
        {'task':'your task describe','action':{'type':'reply','contents':['custom reply']}}
        {'task':'your task describe','action':{'type':'command','contents':['some_scripts.sh']}}
        """
        idx,wrks = self.inter.decode(link)
        self.links.append([idx,wrks])

    def act(self, prompt:str, match_thresh:float = 0.7):
        index = self.inter.embed.embedding(prompt)
        top_score = 0
        top_link = None
        for link in self.links:
            dis = distance(index,link[0]) 
            if dis > top_score and dis >= match_thresh:
                top_score = dis
                top_link = link[1]

        arg = prompt
        rep = []
        if top_link is not None:
            for wrk in top_link:
                r = wrk.do(arg)
                rep.append(r)
                arg = r

        return rep



def __test():
    import time
    linker = Linker()
    time.sleep(1)
    link1 = {'task':'tell a joke','action':{'type':'reply','contents':['Pig can fly with ears']}}
    link2 = {'task':'clock time right now','action':{'type':'command','contents':['date']}}

    linker.add(link1)
    time.sleep(1)
    linker.add(link2)
    time.sleep(1)

    rep = linker.act('what is the time?')
    print(rep)
    time.sleep(1)
    rep = linker.act('I am so boring')
    print(rep)


if __name__ == '__main__':
    __test()

