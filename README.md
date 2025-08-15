# DictaLMClient
Use the Dicta LM demo to accept prompts programmatically, eliminating the need for a GPU.

## Installation
1. Run `pip install playwright`
2. Run `playwright install`

## Run

```
from dicta import DictaBrowser
bot = DictaBrowser()
print(bot.send_prompt("Hello"))
bot.close()
```
