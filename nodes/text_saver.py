import os

class SaveTextToFiles:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
            },
            "optional": {
                "output_directory": ("STRING", {"default": "input"}),
                "file_prefix": ("STRING", {"default": "Scene"}),
            }
        }
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("output_path", "file_prefix")
    FUNCTION = "save_text_to_files"
    CATEGORY = "PromptBatcher"
    def save_text_to_files(self, text: str, output_directory: str = "input", file_prefix: str = "Scene"):
        # Determine the actual output directory
        if os.path.isabs(output_directory):
            # If it's an absolute path, use it as is
            actual_output_directory = output_directory
        else:
            # If it's a relative path, create it inside the 'input' directory
            actual_output_directory = os.path.join(os.getcwd(), "input", output_directory)
        # Ensure the output directory exists
        os.makedirs(actual_output_directory, exist_ok=True)
        # Split the input text into lines
        lines = text.split('\n')
        # Save each non-empty line to a separate file
        file_count = 1
        for line in lines:
            if line.strip():  # Only process non-empty lines
                # Generate file name and check for existing files
                while True:
                    filename = f"{file_prefix}_{file_count:05d}.txt"
                    filepath = os.path.join(actual_output_directory, filename)
                    if not os.path.exists(filepath):
                        break
                    file_count += 1
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(line.strip())
                file_count += 1
        # Return the absolute path and file_prefix
        return (os.path.abspath(actual_output_directory), file_prefix) 