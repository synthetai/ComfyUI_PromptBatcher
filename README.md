# ComfyUI_PromptBatcher

A custom node extension for ComfyUI that enables batch processing of prompts from text files to generate multiple images.

[中文文档](README_CN.md)

## Features

- Load multiple prompt files from a directory
- Filter files by prefix
- Limit the number of files to process
- Start from a specific index
- Force reload option for dynamic workflows
- Save multiple prompts to individual text files at once

## Installation

1. Clone this repository into your ComfyUI custom nodes folder:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/USERNAME/ComfyUI_PromptBatcher.git
```

2. Restart ComfyUI

## Usage

The extension adds the following nodes in the PromptBatcher category:

### Load Prompts From Dir

Loads multiple prompt files from a directory.

#### Node Inputs

- **directory**: Path to the folder containing your prompt text files
- **file_prefix** (optional): Only load files that start with this prefix
- **file_load_cap** (optional): Limit the number of files to load (0 = no limit)
- **start_index** (optional): Start loading from this index in the file list
- **load_always** (optional): Force reload files on every execution

#### Node Outputs

- **PROMPT**: A list of prompt strings loaded from the text files
- **FILE_PATH**: A list of absolute file paths for the loaded files

### Save Text To Files

Saves multiple prompts from a multiline text input to individual text files.

#### Node Inputs

- **text**: A multiline text input, where each line will be saved as a separate prompt file
- **output_directory** (optional): Directory to save the files (default: "input")
- **file_prefix** (optional): Prefix for the generated filenames (default: "Scene")

#### Node Outputs

- **output_path**: The absolute path where files were saved
- **file_prefix**: The prefix used for the files

## Example Workflow

1. Add the "Load Prompts From Dir" node
2. Connect it to a "KSampler (Advanced)" node
3. Set up a batch workflow to process each prompt in sequence

## Example Directory Structure

```
prompts/
├── prompt1.txt
├── prompt2.txt
└── prompt3.txt
```

Each text file should contain a single prompt.


## License

MIT License

## Credits

Created by [Your Name]