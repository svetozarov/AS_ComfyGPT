from .chatgpt_node import ChatGPTNode

NODE_CLASS_MAPPINGS = {
    "ChatGPTNode": ChatGPTNode
}

def load_plugin():
    try:
        from modules import nodes  # Adjust this import if your ComfyUI version differs
    except ImportError:
        print("Module 'modules.nodes' not found. Make sure you have ComfyUI installed.")
        return

    # Если у ComfyUI настроена регистрация через NODE_CLASS_MAPPINGS,
    # этот словарь уже будет использоваться. Однако можно также явно зарегистрировать:
    nodes.register_node(ChatGPTNode)
    print("AS_ComfyGPT plugin successfully registered.")
