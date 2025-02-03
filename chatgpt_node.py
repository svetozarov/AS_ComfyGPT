import time
import openai

class ChatGPTNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key": ("STRING", {"default": ""}),
                "model": ("CHOICE", {"choices": ["gpt-4", "gpt-4-32k", "gpt-3.5-turbo", "gpt-3.5-turbo-16k"], "default": "gpt-4"}),
                "prompt": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "chat_completion"
    CATEGORY = "AS_ComfyGPT Integration"

    def chat_completion(self, api_key, model, prompt):
        print("AS_ComfyGPT: Starting API call...")
        time.sleep(2)  # Artificial delay for demonstration
        openai.api_key = api_key

        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            answer = response["choices"][0]["message"]["content"]
            print("AS_ComfyGPT: API call completed, returning answer.")
            return (answer,)
        except Exception as e:
            print("AS_ComfyGPT: Error encountered:", str(e))
            return (f"Error: {str(e)}",)
