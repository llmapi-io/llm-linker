from core.interpreter import Interpreter
import numpy as np

def distance(embedding1: dict, embedding2: dict) -> float:
    a = embedding1
    b = embedding2
    dot_product = np.dot(a, b)
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    cosine_sim = dot_product / (a_norm * b_norm)
    return cosine_sim

class Linker:
    def __init__(self):
        self.inter = Interpreter()
        self.links = []

    def add(self, link:dict):
        idx,wrks = self.inter.decode(link)
        self.links.append([idx,wrks])

    def act(self, prompt:str):
        index = self.inter.embed.embedding(prompt)
        top_score = 0
        top_link = None
        for link in self.links:
            dis = distance(index,link[0]) 
            if dis > top_score:
                top_score = dis
                top_link = link[1]

        if top_link is not None:
            for wrk in top_link:
                wrk.do()


def __test():
    import time
    linker = Linker()
    time.sleep(1)
    link1 = {'task':'tell a joke','action':{'type':'reply','commands':['you are so funny','is this ok?']}}
    link2 = {'task':'clock time right now','action':{'type':'command','commands':['date']}}

    linker.add(link1)
    time.sleep(1)
    linker.add(link2)
    time.sleep(1)

    linker.act('make me laugh')
    time.sleep(1)
    linker.act('what is the time?')
    time.sleep(1)
    linker.act('I am so boring')


if __name__ == '__main__':
    __test()

