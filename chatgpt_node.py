import time
from openai import OpenAI

class ChatGPTNode:
    HIDDEN = ("model",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key_file": ("STRING", {"default": ""}),
                "model": (("gpt-4", "gpt-4-32k", "gpt-3.5-turbo", "gpt-3.5-turbo-16k"), {"default": "gpt-4"}),
                "prompt": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "chat_completion"
    CATEGORY = "AS_ComfyGPT"  # Node will appear under the name AS_ComfyGPT

    def chat_completion(self, api_key_file, model, prompt):
        try:
            with open(api_key_file, "r") as f:
                key = f.read().strip()
        except Exception as e:
            return (f"Error reading API key file: {str(e)}",)

        print("AS_ComfyGPT: Starting API call...")
        time.sleep(2)  # Artificial delay for demonstration

        client = OpenAI(api_key=key)
        try:
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            answer = completion.choices[0].message.content
            print("AS_ComfyGPT: API call completed, returning answer.")
            return (answer,)
        except Exception as e:
            print("AS_ComfyGPT: Error encountered:", str(e))
            return (f"Error: {str(e)}",)
