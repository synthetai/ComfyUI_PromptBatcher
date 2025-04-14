import os
import re

class LoadPromptsFromDir:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "directory": ("STRING", {"default": ""}),
            },
            "optional": {
                "file_prefix": ("STRING", {"default": ""}),
                "file_load_cap": ("INT", {"default": 0, "min": 0, "step": 1}),
                "start_index": ("INT", {"default": 0, "min": 0, "step": 1}),
                "load_always": ("BOOLEAN", {"default": False, "label_on": "enabled", "label_off": "disabled"}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("PROMPT", "FILE_PATH")
    OUTPUT_IS_LIST = (True, True)

    FUNCTION = "load_prompts"

    CATEGORY = "PromptBatcher"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        if 'load_always' in kwargs and kwargs['load_always']:
            return float("NaN")
        else:
            return hash(frozenset(kwargs.items()))

    def load_prompts(self, directory: str, file_prefix: str = "", file_load_cap: int = 0, start_index: int = 0, load_always=False):
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory '{directory}' cannot be found.")
        
        dir_files = os.listdir(directory)
        if len(dir_files) == 0:
            raise FileNotFoundError(f"No files in directory '{directory}'.")

        # Filter files based on prefix and .txt extension
        if file_prefix:
            txt_files = [f for f in dir_files if f.lower().startswith(file_prefix.lower()) and f.lower().endswith('.txt')]
        else:
            txt_files = [f for f in dir_files if f.lower().endswith('.txt')]
        
        if not txt_files:
            raise FileNotFoundError(f"No matching .txt files found in directory '{directory}' with prefix '{file_prefix}'.")

        # Custom sorting function
        def sort_key(filename):
            # Extract the number from the filename
            match = re.search(r'\d+', filename)
            if match:
                return int(match.group())
            return filename

        # Sort the files using the custom sort key
        txt_files = sorted(txt_files, key=sort_key)
        txt_files = [os.path.join(directory, x) for x in txt_files]

        # Start at start_index
        txt_files = txt_files[start_index:]

        prompts = []
        file_paths = []

        limit_files = False
        if file_load_cap > 0:
            limit_files = True
        file_count = 0

        for txt_path in txt_files:
            if limit_files and file_count >= file_load_cap:
                break
            try:
                with open(txt_path, 'r', encoding='utf-8') as file:
                    prompt = file.read().strip()
                    prompts.append(prompt)
                    file_paths.append(os.path.abspath(txt_path))
                    file_count += 1
            except Exception as e:
                print(f"Error reading file {txt_path}: {str(e)}")

        return (prompts, file_paths) 