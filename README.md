## :eyes: What is llm-linker?
llm-linker hope to connect natural language requests with relevant structured actions or responses through the semantic understanding ability of LLM.

```mermaid
graph LR
task_prompt-->|embedding| index_map --> actions.->commands.-> image_gen
command.-> cv_task
command.-> program
command.-> ...
query_prompt-->|embedding| index_map 
actions.->reply
actions.->regen .-> more_context
```

### TODOs

- [ ] support `requests` type, for directly link to OpenAPIs.
- [ ] support linkDB, to store links locally.
- [ ] combine with `Decision Tree` ?

## :point_right: Try it

```
# Get Apikey on https://llmapi.io

python3 run.py --apikey=your_api_key --links=links.txt --query='what is the time?'

# some.sh will be executed
```

`python3 run.py --links=links.txt --query="写一个登录页面" --apikey=********************************`

result:

[demo](demo/html.png)

## :art: Linker schema
During runtime，user input query prompt, prompt encoded as `embedding`，then match with linker's `task`，finally you can do anything through actions with simple language prompt.

> User's query prompt is always provided as a parameter to `actions`.

The following linker description as a example:
```json
{
    "task" : "play music 'ten years'",
    "actions" : [
        {
            "type" : "command",
            "content" : "./play.sh",
            "input" : "_NONE_"
        }
     ]
}
```
The `task` in linker is a prompt to be encoded as `embedding`，then the embedding index map with actions.
The `actions` described in detail what to do when user's query matched task.
The `type` in `actions` should be `reply` `command` or `regen`:
 - `reply`: you can pin the content of replies when `task` was matched.
 - `command`: you can run a set of scripts or local programs when `task` was matched.
 - `regen`: you can re-ask LLM (such as chatgpt) based on task input to get new responses when `task` was matched.
The `content` in `actions` is your reply content or shell or prompt for regen.
The `input` in `actions` means if your content need a input when proccessing:`_NONE_`,`_PROMPT_`,`_OUTPUT_`.

### some linker demos

1. Using `reply` type
```json
{
    "task" : "tell your name", "actions" : [{ "type" : "reply", "content" : "I'm llm-linker!","input":"_NONE_"}]
}
```
> user's input: what's your name?
> 
> linker's output: I'm llm-linker!

2. Using `command` type
```json
{
    "task" : "get current time", "actions" : [{ "type" : "command", "content" : "./get_time.sh","input":"_NONE_"}]
}

```

`get_time.sh`:
```shell
#! /bin/sh
date +"%Y-%m-%d %H:%M:%S"
```

> user's input: what's the time?
> 
> linker's output: 2023-04-11 11:22:33

2. Using `regen` type
```json
{
    "task" : "do math addition", "actions" : [{ "type" : "regen", "content" : "Calculate step by step:","input":"_PROMPT_"}]
}

```

> user's input: 1+1=?
> 
> linker's output(use `chatgpt`):
```
Sure, I'd be happy to help you calculate step by step!
1 + 1 = 2
Explanation:
1. Start with the leftmost number: 1 + 1
2. Add the two numbers together: 1 + 1
3. The answer is 2. 
```

## :scroll: Interface description

> Very simple, only TWO api

The only thing you need to use is the `Linker` class.

Interface in `Linker`:

### 1. add (link:dict)

use this interface to dynamic add linkers:

```
link = Linker(apikey='xxx') # apikey can get on llmapi.io, use it to talk with LLMs online.
link.add({"task" : "tell your name", "actions" : [{"type" : "reply", "content" : "I'm llm-linker!", "input":"_NONE_"} ]})

# Done!
```

### 2. act (prompt:str, match_thresh:float = 0.7)

use this interface to match `task` and execute actions for user's query:

> match_thresh is the threshold for embedding similarity

```
link.act('what is your name?')

# Done!
```

### :star2: If you like this project, please follow us and star it, let's play together! :heart:



