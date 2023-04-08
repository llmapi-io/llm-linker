## 什么是llm-linker?
llm-linker 希望通过llm的语义理解能力，将自然语言命令（或需求）与相关的结构化动作或回应连接。例如以下的linker描述:

```json
{
		"prompt" : "play music 'ten years'",
		"action" : {
				"type" : "execute",
				"commands" : [
						"./play.sh --name 'ten years'"
				]
		}
}
```
linker中的prompt将被解析成`embedding`，然后与相关的action进行map

在runtime，用户输入query prompt, prompt被解析成`embedding`，然后与linkers进行比对，根据最匹配的linker执行action

```mermaid
graph LR
preset_prompt-->|index| index_map --> action.->commands
query_prompt-->|index| index_map 
action.->reply
action.->...
```
