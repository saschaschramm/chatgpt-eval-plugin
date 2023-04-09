# ChatGPT Eval Plugin
This is a very simple example of a plugin for ChatGPT. The plugin passes a string to the Python `eval` built-in.

## Install
```console
pip install -r requirements.txt
```

## Run the Plugin
```console
uvicorn main:app --port 8000
```

## Add the Plugin to ChatGPT
1. Visit https://chat.openai.com/
2. Click on Plugins -> Plugin Store -> Develop your own plugin
2. Add the domain localhost:8000 and click "Find manifest file"

## Example
In order to test the plugin, you can enter `13+37` in the chat window. The plugin will evaluate the expression and return the result.



