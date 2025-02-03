from .chatgpt_node import ChatGPTNode

def load_plugin():
    """
    This function registers the ChatGPT node in ComfyUI.
    It is called automatically when the plugin is loaded.
    """
    try:
        from modules import nodes  # Adjust this import if your ComfyUI version differs
    except ImportError:
        print("Module 'modules.nodes' not found. Make sure you have ComfyUI installed.")
        return

    nodes.register_node(ChatGPTNode)
    print("AS_ComfyGPT plugin successfully registered.")
