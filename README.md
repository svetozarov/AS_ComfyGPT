# AS_ComfyGPT

AS_ComfyGPT is a plugin for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that integrates ChatGPT using the OpenAI API.

## Features

- Accepts an API key, model name, and a text prompt.
- Sends a synchronous request to ChatGPT and returns its response.
- The workflow waits for the node to finish processing before proceeding.

## Requirements

- ComfyUI (installed and configured)
- Python 3.7+
- The following Python package (automatically installed via pip):
  - openai (>=0.27.0)

Install the required package using:

```bash
pip install openai
