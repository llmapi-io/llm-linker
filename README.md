## what is llm-linker?
llm-linker hope to connect natural language requests with relevant structured actions or responses through the semantic understanding ability of LLM. For example, the following linker description:

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

During runtime，user input query prompt, prompt encoded as `embedding`，then match with linkers，finally you can do actions with simple language prompt.

```mermaid
graph LR
preset_prompt-->|embedding| index_map --> action.->commands.-> ...
query_prompt-->|embedding| index_map 
action.->reply
```

## Try it

```
# Get Apikey on https://llmapi.io

python3 run.py --apikey=your_api_key --links=links.txt --query='what is the time?'

# some.sh will be executed
```
