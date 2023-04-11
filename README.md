## :eyes: What is llm-linker?
llm-linker hope to connect natural language requests with relevant structured actions or responses through the semantic understanding ability of LLM.

```mermaid
graph LR
task_prompt-->|embedding| index_map --> action.->commands.-> ...
query_prompt-->|embedding| index_map 
action.->reply
```

## :point_right: Try it

```
# Get Apikey on https://llmapi.io

python3 run.py --apikey=your_api_key --links=links.txt --query='what is the time?'

# some.sh will be executed
```

## :art: Linker schema
During runtime，user input query prompt, prompt encoded as `embedding`，then match with linker's `task`，finally you can do anything through actions with simple language prompt.

> User's query prompt is always provided as a parameter to `action`.

The following linker description as a example:
```json
{
    "task" : "play music 'ten years'",
    "action" : {
        "type" : "command",
        "contents" : [
            "./play.sh --name 'ten years'"
	]
    }
}
```
The `task` in linker is a prompt to be encoded as `embedding`，then the embedding index map with action.
The `action` described in detail what to do when user's query matched task.
The `type` in `action` should be `reply` `command` or `regen`:
 - `reply`: you can pin the content of replies when `task` was matched.
 - `command`: you can run a set of scripts or local programs when `task` was matched.
 - `regen`: you can re-ask LLM (such as chatgpt) based on task input to get new responses when `task` was matched.

### some linker demo

1. Using `reply` type
```json
{
    "task" : "tell your name", "action" : { "type" : "reply", "contents" : [ "I'm llm-linker!" ] }
}
```
> user's input: what's your name?
> linker's output: I'm llm-linker!

2. Using `command` type
```json
{
    "task" : "get current time", "action" : { "type" : "command", "contents" : [ "./get_time.sh" ] }
}

```

`get_time.sh`:
```shell
#! /bin/sh
date +"%Y-%m-%d %H:%M:%S"
```

> user's input: what's the time?
> linker's output: 2023-04-11 11:22:33

2. Using `regen` type
```json
{
    "task" : "do math addition", "action" : { "type" : "regen", "contents" : [ "Calculate step by step:"] }
}

```

> user's input: 1+1=?
> linker's output(use `chatgpt`):
```
Sure, I'd be happy to help you calculate step by step!
1 + 1 = 2
Explanation:
1. Start with the leftmost number: 1 + 1
2. Add the two numbers together: 1 + 1
3. The answer is 2. 
```

## Interface description

> Very simple, only TWO api

The only thing you need to use is the `Linker` class.

Interface in `Linker`:

### add(link:dict)

use this interface to dynamic add linkers:

```
link = Linker(apikey='xxx') # apikey can get on llmapi.io, use it to talk with LLMs online.
link.add({"task" : "tell your name", "action" : { "type" : "reply", "contents" : [ "I'm llm-linker!" ] }})

# Done!
```

### act(prompt:str, match_thresh:float = 0.7)

use this interface to match `task` and execute actions for user's query:

> match_thresh is the threshold for embedding similarity

```
link.act('what is your name?')

# Done!
```




