from core.linker import Linker
import argparse as ap
import json
import time
import os


def _parse_arg():
    parse = ap.ArgumentParser(description="Link chatgpt to your shells") 
    parse.add_argument('--apikey', type=str, help='Your api key for https://llmapi.io')
    parse.add_argument('--links', type=str, default='links.txt', help="Links describe file")
    parse.add_argument('--query', type=str, default='what is the time?',help='Your query')
    arg = parse.parse_args()
    return arg

if __name__ == '__main__':
    arg = _parse_arg()
    linker = Linker(arg.apikey)
    with open(arg.links) as f:
        lines = f.readlines()
        for line in lines:
            linker.add(json.loads(line))
            time.sleep(0.5)

    rep = linker.act(arg.query)
    print(rep)
