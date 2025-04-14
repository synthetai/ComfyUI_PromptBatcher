from .prompt_batcher import LoadPromptsFromDir
from .text_saver import SaveTextToFiles

NODE_CLASS_MAPPINGS = {
    "LoadPromptsFromDir": LoadPromptsFromDir,
    "SaveTextToFiles": SaveTextToFiles
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadPromptsFromDir": "Load Prompts From Dir",
    "SaveTextToFiles": "Save Text To Files"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 