from .prompt_batcher import LoadPromptsFromDir

NODE_CLASS_MAPPINGS = {
    "LoadPromptsFromDir": LoadPromptsFromDir
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadPromptsFromDir": "Load Prompts From Dir"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 